
from models import (
    users_model,
    book_model,
    transactions_model 
)
from schema import Transactions
from sqlalchemy.future import select
from sqlalchemy import and_, or_, desc, update, delete, join, outerjoin
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from service import ResponseOutCustom, loging

log = loging()

async def create_new_trasancation(request: Transactions ,user:dict, db: AsyncSession):
    async with db as session:
        try:
            getBook = await get_book_by_id(request.book_id, db)
            if not getBook: 
                return ResponseOutCustom(
                    message_id="02",
                    status="Buku tidak ditemukan",
                    list_data=[]
                )
            valPinjaman = await get_transac_by_id(request.book_id, db)
            if valPinjaman.list not in (None, []):
                if user['username'] == valPinjaman.list['id_user']:
                    return ResponseOutCustom(
                        message_id="02",
                        status=f"User {user['username']} masih meminjam buku dan belum di kembalikan, harap mengebalikan buku pinjaman terlebih dahulu",
                        list_data=[]
                    )
                
                if valPinjaman.list['status'] == 'terpinjam':
                    return ResponseOutCustom(
                        message_id="02",
                        status="Buku sedang dalam masa pinjaman",
                        list_data=valPinjaman.list
                    )
            
            trx = transactions_model.Transactions
            data = trx(
                book_id=getBook['id'],
                jenis_transaksi=request.jenis_transaksi,
                status="terpinjam",
                id_user = user['username'],
                keterangan=request.keterangan,
                created_at=datetime.now()
            )
            session.add(data)

            book = book_model.Book
            update_trx = update(book).where(book.id == getBook['id']).values(
                book_status = "terpinjam",
                book_date_brw = datetime.now(),
                book_date_drs = 30,
            )
            await session.execute(update_trx)

            await session.commit()

            return ResponseOutCustom(message_id="00", status="Tambah data pinjam buku berhasil", list=request)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f"{str(e)}", list_data=[])


async def get_list_pinjman_buku(limit, page, keyword, db: AsyncSession):
    async with db as session:
        try:
            offset = page * limit
            terms = []

            trx = transactions_model.Transactions

            if keyword not in (None, [],''):
                terms.append(
                    or_(
                        (trx.jenis_transaksi.ilike(f'%{keyword}%')),
                        (trx.status.ilike(f'%{keyword}%'))
                    )
                )
                
            if len(terms) > 0:
                query_stmt = select(
                    trx
                    ).filter(and_(*(terms), trx.status == 'terpinjam')
                ).limit(limit).offset(offset).order_by(trx.created_at)
            else:
                query_stmt = select(
                    trx
                ).where(trx.status == 'terpinjam').limit(limit).offset(offset).order_by(trx.created_at)
            
            proxy_rows = await session.execute(query_stmt)
            result = proxy_rows.scalars().all()
            datas = jsonable_encoder(result)
            dt = []
            for i in datas:  
                getDetailBuku = await get_book_by_id(i['book_id'], db)
                if not getDetailBuku: 
                    continue

                dt.append({
                    "id": i['id'],
                    "book_id": i['book_id'],
                    "jenis_transaksi": i['jenis_transaksi'],
                    "judul_buku": getDetailBuku.get('book_name', ''),
                    "tanggal_pinjam_buku": getDetailBuku.get('book_date_brw', ''),
                    "tanggal_kembali_bukus": getDetailBuku.get('book_date_rtn', ''),
                    "durasi_pinjam_buku": f"{getDetailBuku.get('book_date_drs', '')} hari",
                    "status": i['status'],
                    "id_user": i['id_user'],
                    "keterangan": i['keterangan'],
                    "created_at": i['created_at'],
                })
            

            status = 'Berhasil' if datas not in (None, []) else 'Data tidak ditemukan'

            return ResponseOutCustom(message_id="00", status=status, list_data=dt)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])

async def get_list_buku(limit, page, keyword, db: AsyncSession):
    async with db as session:
        try:
            offset = page * limit
            terms = []

            trx = transactions_model.Transactions

            if keyword not in (None, [],''):
                terms.append(
                    or_(
                        (trx.jenis_transaksi.ilike(f'%{keyword}%')),
                        (trx.status.ilike(f'%{keyword}%'))
                    )
                )
                
            if len(terms) > 0:
                query_stmt = select(
                    trx
                    ).filter(*(terms)
                ).limit(limit).offset(offset).order_by(trx.created_at)
            else:
                query_stmt = select(
                    trx
                ).limit(limit).offset(offset).order_by(trx.created_at)
            
            proxy_rows = await session.execute(query_stmt)
            result = proxy_rows.scalars().all()
            datas = jsonable_encoder(result)
            dt = []
            for i in datas:  
                getDetailBuku = await get_book_by_id(i['book_id'], db)
                if not getDetailBuku: 
                    continue

                dt.append({
                    "id": i['id'],
                    "book_id": i['book_id'],
                    "jenis_transaksi": i['jenis_transaksi'],
                    "judul_buku": getDetailBuku.get('book_name', ''),
                    "tanggal_pinjam_buku": getDetailBuku.get('book_date_brw', ''),
                    "tanggal_kembali_bukus": getDetailBuku.get('book_date_rtn', ''),
                    "durasi_pinjam_buku": f"{getDetailBuku.get('book_date_drs', '')} hari",
                    "status": i['status'],
                    "id_user": i['id_user'],
                    "keterangan": i['keterangan'],
                    "created_at": i['created_at'],
                })
            

            status = 'Berhasil' if datas not in (None, []) else 'Data tidak ditemukan'

            return ResponseOutCustom(message_id="00", status=status, list_data=dt)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])


async def get_transac_by_id(request,db: AsyncSession):
    async with db as session:
        try:
            trx = transactions_model.Transactions
            query_stmt = select(trx).where(trx.id == request)
            proxy_rows = await session.execute(query_stmt)
            result = proxy_rows.scalars().first()
            datas = jsonable_encoder(result)
            return ResponseOutCustom(
                message_id="00",
                status="Berhasil",
                list_data=datas
            )
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])

async def create_pengembalian_buku(request: Transactions, user_info: dict , db: AsyncSession):
    async with db as session:
        try:
            if (request.jenis_transaksi.upper() != "K"):
                return ResponseOutCustom(
                    message_id="02",
                    status="Jenis transaksi tidak valid",
                    list_data=[]
                )
            
            getBook = await get_book_by_id(request.book_id, db)
            if not getBook: 
                return ResponseOutCustom(
                    message_id="02",
                    status="Buku tidak ditemukan",
                    list_data=[]
                )
            
            trx = transactions_model.Transactions
            update_pengembalian = update(trx).where(trx.book_id == getBook['id']).values(
                book_id=getBook['id'],
                jenis_transaksi=request.jenis_transaksi.upper(),
                status="tersedia",
                id_user = user_info['username'],
                keterangan=request.keterangan,
                created_at=datetime.now()
            )
            await session.execute(update_pengembalian)

            book = book_model.Book
            update_trx = update(book).where(book.id == getBook['id']).values(
                book_status = "tersedia",
                book_date_drs = None,
                book_date_rtn = datetime.now(),
            )
            await session.execute(update_trx)

            await session.commit()

            return ResponseOutCustom(message_id="00", status="Pengembalian buku berhasil", list=request)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f"{str(e)}", list_data=[])


async def get_book_by_id(request,db: AsyncSession):
    async with db as session:
        try:
            query_stmt = select(book_model.Book).where(book_model.Book.id == request)
            proxy_rows = await session.execute(query_stmt)
            result = proxy_rows.scalars().first()
            datas = jsonable_encoder(result)
            return datas
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])

# async def get_book_by_id(request,db: AsyncSession):
#     async with db as session:
#         try:
#             query_stmt = select(book_model.Book).where(book_model.Book.id == request)
#             proxy_rows = await session.execute(query_stmt)
#             result = proxy_rows.scalars().first()
#             datas = jsonable_encoder(result)

#             status = 'Berhasil' if datas not in (None, []) else 'Data tidak ditemukan'

#             return ResponseOutCustom(message_id="00", status=status, list_data=datas)
        
#         except Exception as e:
#             return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])


# async def update_book_by_id(data:Book,db: AsyncSession):
#     async with db as session:
#         try:
            
#             # get data anak
#             book = book_model.Book
#             query_stmt = select(book).where(book.id==data.id)
            
#             log.info(query_stmt)
#             proxy_rows = await session.execute(query_stmt)
#             result = proxy_rows.scalars().first()
            
#             if result in (None, []):
#                 return ResponseOutCustom(message_id="02", status=f'Data buku dengan {data.id} tidak ditemukan', list_data=[])

#             update_data_book = update(book).where(book.id==result.id).values(
#                 book_name = data.book_name,
#                 book_category = data.book_category,
#                 book_qty = data.book_qty,
#                 book_price = data.book_price,
#                 book_desc = data.book_desc

#             )
#             await session.execute(update_data_book)
#             await session.commit()

#             return ResponseOutCustom(message_id="00", status=f"Pembaharuan buku {data.id} berhasil", list_data=data)
        
#         except Exception as e:
#             return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])
        
# async def delete_book_by_id(data,db: AsyncSession):
#     async with db as session:
#         try:
#             book = book_model.Book
#             query_stmt = select(book).where(book.id==data)
#             proxy_rows = await session.execute(query_stmt)
#             result = proxy_rows.scalars().first()

#             if result in (None, []):
#                 return ResponseOutCustom(message_id="02", status=f'Data buku dengan ID {data} tidak ditemukan', list_data=[])

#             delete_data_cucu = delete(book).where(book.id==result.id)
#             await session.execute(delete_data_cucu)
#             await session.commit()

#             return ResponseOutCustom(message_id="00", status=f"Hapus data buku ID {data} berhasil", list_data=data)
        
#         except Exception as e:
#             return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])
