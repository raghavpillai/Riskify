import React, { useEffect } from 'react';
import { useState } from 'react';
import { useRouter } from 'next/router'
import Navbar from '../components/Navbar'
import Form02f from '../components/form-02f';

function Onboarding01() {

  let router = useRouter();

  const [state, setState] = useState(false);

  useEffect(() =>{
    if(router.query.p === 'true'){
        setState(true)
    }
  },[])

  const handleClick = () => {
    let form = document.getElementById('form') as HTMLFormElement;
    console.log(form.elements)

    if((form.elements[5] as HTMLFormElement).checked === true){
        console.log('reroute to dashboard, rebalance = true')
    }
    if((form.elements[6] as HTMLFormElement).checked === true){
        console.log('reroute to dashboard, rebalance = false')
    }
    // router.push('/form-03')
  }
    
  return (
    <>
    <Navbar />

    {!state && 
    <Form02f />
    }

    {state &&
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
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <div className="px-4 py-8 w-[50%] self-center shadow-xl rounded-md">
              <div className="max-w-md mx-auto">

                <h1 className="text-3xl text-slate-800 font-bold mb-6">Please Enter Your Portfolio Weight Percentages</h1>
                {/* Form */}
                <form id="form">
                  <div className="space-y-3 mb-8">
                    <label className="relative block cursor-pointer">
                      <div>
                        <label className="block text-sm font-medium mb-1" htmlFor="company-name">Stocks <span className="text-rose-500">*</span></label>
                        <input id="stocks" className="form-input w-full shadow-sm rounded focus:outline-none focus:border-2 focus:border-[#1ddcdc] p-[1rem]" type="text" />
                      </div>
                    </label>
                    <label className="relative block cursor-pointer">
                      <div>
                        <label className="block text-sm font-medium mb-1" htmlFor="company-name">Bonds<span className="text-rose-500">*</span></label>
                        <input id="bonds" className="form-input w-full shadow-sm rounded focus:outline-none focus:border-2 focus:border-[#1ddcdc] p-[1rem]" type="text" />
                      </div>
                    </label>
                    <label className="relative block cursor-pointer">
                      <div>
                        <label className="block text-sm font-medium mb-1" htmlFor="company-name">Cash & Capital <span className="text-rose-500">*</span></label>
                        <input id="capital" className="form-input w-full shadow-sm rounded focus:outline-none focus:border-2 focus:border-[#1ddcdc] p-[1rem]" type="text" />
                      </div>
                    </label>
                    <label className="relative block cursor-pointer">
                      <div>
                        <label className="block text-sm font-medium mb-1" htmlFor="company-name">Real Estate <span className="text-rose-500">*</span></label>
                        <input id="real-estate" className="form-input w-full shadow-sm rounded focus:outline-none focus:border-2 focus:border-[#1ddcdc] p-[1rem]" type="text" />
                      </div>
                    </label>
                    <label className="relative block cursor-pointer">
                      <div>
                        <label className="block text-sm font-medium mb-1" htmlFor="company-name">Commodities <span className="text-rose-500">*</span></label>
                        <input id="commodities" className="form-input w-full shadow-sm rounded focus:outline-none focus:border-2 focus:border-[#1ddcdc] p-[1rem]" type="text" />
                      </div>
                    </label>

                    <label className="block text-sm font-medium mb-1" htmlFor="company-name">Would You Like to Rebalance Your Portfolio? <span className="text-rose-500">*</span></label>
                    <label className="relative block cursor-pointer">
                      <input type="radio" name="radio-buttons" className="peer sr-only" defaultChecked />
                      <div className="flex items-center bg-white text-sm font-medium text-slate-800 p-4 rounded border border-slate-200 hover:border-slate-300 shadow-sm duration-150 ease-in-out">
                        <svg className="w-6 h-6 shrink-0 fill-current mr-4" viewBox="0 0 24 24">
                          <path className="text-[#1ddcdcb0]" d="m12 10.856 9-5-8.514-4.73a1 1 0 0 0-.972 0L3 5.856l9 5Z" />
                          <path className="text-[#1ddcdc92]" d="m11 12.588-9-5V18a1 1 0 0 0 .514.874L11 23.588v-11Z" />
                          <path className="text-[#1ddcdc74]" d="M13 12.588v11l8.486-4.714A1 1 0 0 0 22 18V7.589l-9 4.999Z" />
                        </svg>
                        <span>Yes</span>
                      </div>
                      <div className="absolute inset-0 border-2 border-transparent peer-checked:border-[#1ddcdc] rounded pointer-events-none" aria-hidden="true"></div>
                    </label>
                    <label className="relative block cursor-pointer">
                      <input type="radio" name="radio-buttons" className="peer sr-only" />
                      <div className="flex items-center bg-white text-sm font-medium text-slate-800 p-4 rounded border border-slate-200 hover:border-slate-300 shadow-sm duration-150 ease-in-out">
                        <svg className="w-6 h-6 shrink-0 fill-current mr-4" viewBox="0 0 24 24">
                          <path className="text-[#1ddcdcb0]" d="m12 10.856 9-5-8.514-4.73a1 1 0 0 0-.972 0L3 5.856l9 5Z" />
                        </svg>
                        <span>No </span>
                      </div>
                      <div className="absolute inset-0 border-2 border-transparent peer-checked:border-[#1ddcdc] rounded pointer-events-none" aria-hidden="true"></div>
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

    </main>}
    </>
  );
}

export default Onboarding01;