import React from 'react';
import { useState } from 'react';
import { useRouter } from 'next/router'
import Navbar from './Navbar'

function Form02f() {

  let router = useRouter();

  const handleClick = () => {
    let form = document.getElementById('form') as HTMLFormElement;
    console.log(form.elements[0])
    router.push('/form-03')
  }
    
  return (
    <>
    <main className="bg-[#efefef]">

      <div className="relative flex">

        {/* Content */}
        <div className="w-full">

          <div className="min-h-screen h-full flex flex-col after:flex-1">

            <div className="flex-1">

              {/* Header */}
              <div className="flex items-center justify-between h-16 px-4 sm:px-6 lg:px-8">
                {/* Logo */}
              </div>

              {/* Progress bar */}
              <div className="px-4 pt-12 pb-8">
                <div className="max-w-md mx-auto w-full">
                  <div className="relative">
                    <div className="absolute left-0 top-1/2 -mt-px w-full h-0.5 bg-slate-200" aria-hidden="true"></div>
                    <ul className="relative flex justify-between w-full">
                      <li>
                        <a className="flex items-center justify-center w-6 h-6 rounded-full text-xs font-semibold bg-[#ffffff] text-slate-500" href="/form-01">1</a>
                      </li>
                      <li>
                        <a className="flex items-center justify-center w-6 h-6 rounded-full text-xs font-semibold bg-[#1ddcdc] text-white" href="/form-02">2</a>
                      </li>
                      <li>
                        <a className="flex items-center justify-center w-6 h-6 rounded-full text-xs font-semibold bg-[#ffffff] text-slate-500" href="/form-03">3</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <div className="px-4 py-8 w-[50%] self-center shadow-xl rounded-md">
              <div className="max-w-md mx-auto">

                <h1 className="text-3xl text-slate-800 font-bold mb-6">Please Enter Your Current Capital Amount</h1>
                {/* Form */}
                <form id="form">
                  <div className="space-y-3 mb-8">
                    <label className="relative block cursor-pointer">
                      <div>
                        <label className="block text-sm font-medium mb-1" htmlFor="company-name">Cash & Capital <span className="text-rose-500">*</span></label>
                        <input id="capital" className="form-input w-full shadow-sm rounded focus:outline-none focus:border-2 focus:border-[#1ddcdc] p-[1rem]" type="text" />
                      </div>
                    </label>
                  </div>
                  <div className="flex items-center justify-between">
                    <a className="btn bg-[#1ddccc] hover:bg-[#1ddcdccc] text-white ml-auto rounded-full p-2" onClick={handleClick}>Next Step -&gt;</a>
                  </div>
                </form>

              </div>
            </div>

          </div>

        </div>

      </div>

    </main>
    </>
  );
}

export default Form02f;