import Head from 'next/head';
import { FaFacebook, FaLinkedinIn, FaRegEnvelope, FaTwitter } from 'react-icons/fa';
import { MdLockOutline } from 'react-icons/md';
import React from 'react';

const Login = () => {
  return (
    <div className='flex flex-col items-center justify-center min-h-screen py-2 bg-gray-100'>
    <Head>
      <title>login Page e-Library</title>
      <link rel="icon" href="/favicon.ico" />
    </Head>
    <main className='flex flex-col items-center justify-center w-full flex-1 px-20 text-center'>
      <div className='bg-white rounded-2xl shadow-2xl flex w-2/3 max-w-screen-4xl'>
        <div className='w-3/5 p-5'>
          <div className='text-left font-bold'>
            <span className='text-green-500'>Application System of</span> e-Library
          </div>
          <div className='py-10'>
            <h2 className='text-3xl font-bold text-green-500 mb-2'>Sign in to e-Lbrary</h2>
            <div className='border-2 w-10 border-green-500 inline-block mb-2'></div>
            <div className='flex justify-center my-2'>
              <a href="#" className='border-2 border-gray-200 rounded-full p-3 mx-1'><FaFacebook className='text-sm' /></a>
              <a href="#" className='border-2 border-gray-200 rounded-full p-3 mx-1'><FaLinkedinIn className='text-sm' /></a>
              <a href="#" className='border-2 border-gray-200 rounded-full p-3 mx-1'><FaTwitter className='text-sm' /></a>
            </div>
            <p className='text-gray-200'>or user your account</p>
            <div className='flex flex-col items-center'>
              <div className='bg-gray-100 w-64 p-2 flex items-center mb-3 rounded-full'><FaRegEnvelope className='text-gray-400 mr-2' />
                <input type="email" name='email' placeholder='Your email' className='bg-gray-100 outline-none text-sm flex-1' />
              </div>
              <div className='bg-gray-100 w-64 p-2 flex items-center mb-3 rounded-full'><MdLockOutline className='text-gray-400 mr-2' />
                <input type="password" name='password' placeholder='Your password ' className='bg-gray-100 outline-none text-sm flex-1' />
              </div>
              <div className='flex justify-between w-64 mb-5'>
                <label className='flex items-center text-xs'><input type="checkbox" name='remember' /> Remember Me</label>
                <a href="#" className='text-xs'>Forgot Password!</a>
              </div>
            </div>
            <a href="#" className='border-2 border-green-500 text-green-500 rounded-full px-12 py-2 inline-block font-semibold hover:bg-green-500 hover:text-white'>Sign In</a>
          </div>
        </div>
        {/* Sign In section */}
        <div className='w-2/5 bg-green-500 text-white rounded-tr-2xl rounded-br-2xl py-36 px-12'>
          <h2 className='text-3xl font-bold mb-2'>Hello, People</h2>
          <div className='border-2 w-10 border-white inline-block mb-2'></div>
          <p className='mb-10'>Fill up personal information and start journey with us</p>
          <a href="/register" className='border-2 border-white rounded-full px-12 py-2 inline-block font-semibold hover:bg-white hover:text-green-500'>Sign Up</a>
        </div>
      </div>

    </main>

  </div>
  );
};

export default Login;
