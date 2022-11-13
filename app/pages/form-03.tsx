import React, { useEffect } from 'react';
import { useState } from 'react';
import { useRouter } from 'next/router'
import Navbar from '../components/Navbar'

function Onboarding01() {

  let router = useRouter();

  const [state, setState] = useState(false);

  const handleClick = () => {
    let form = document.getElementById('form') as HTMLFormElement;

    let obj = JSON.parse(localStorage.getItem('obj') || '{}')
    console.log(obj)

    for(let i=0; i < form.elements.length; i++){
      if((form.elements[i] as HTMLFormElement).checked === true){
        obj['balance'] = (form.elements[i] as HTMLFormElement).id
        break
      }
    }
    localStorage.setItem('obj', JSON.stringify(obj))
    router.push('/dashboard')
  }

  return (
    <>
    <Navbar />

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
                        <a className="flex items-center justify-center w-6 h-6 rounded-full text-xs font-semibold bg-[#ffffff] text-slate-500" href="/form-02">2</a>
                      </li>
                      <li>
                        <a className="flex items-center justify-center w-6 h-6 rounded-full text-xs font-semibold bg-[#1ddcdc] text-white" href="/form-03">3</a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>

            <div className="px-4 py-8 w-[50%] self-center shadow-xl rounded-md">
              <div className="max-w-md mx-auto">

                <h1 className="text-3xl text-slate-800 font-bold mb-6">Please Select a Risk Tolerance (ranked from risky to not risky)</h1>
                {/* Form */}
                <form id="form">
                  <div className="space-y-3 mb-8">
                    <label className="block text-sm font-medium mb-1" htmlFor="company-name">Risk Tolerance<span className="text-rose-500">*</span></label>
                    <label className="relative block cursor-pointer">
                      <input type="radio" name="radio-buttons" className="peer sr-only" defaultChecked id="ultra_aggressive"/>
                      <div className="flex items-center bg-white text-sm font-medium text-slate-800 p-4 rounded border border-slate-200 hover:border-slate-300 shadow-sm duration-150 ease-in-out">
                        <span>Ultra Aggressive</span>
                      </div>
                      <div className="absolute inset-0 border-2 border-transparent peer-checked:border-[#1ddcdc] rounded pointer-events-none" aria-hidden="true"></div>
                    </label>
                    <label className="relative block cursor-pointer">
                      <input type="radio" name="radio-buttons" className="peer sr-only" defaultChecked id="aggressive"/>
                      <div className="flex items-center bg-white text-sm font-medium text-slate-800 p-4 rounded border border-slate-200 hover:border-slate-300 shadow-sm duration-150 ease-in-out">
                        <span>Aggressive</span>
                      </div>
                      <div className="absolute inset-0 border-2 border-transparent peer-checked:border-[#1ddcdc] rounded pointer-events-none" aria-hidden="true"></div>
                    </label>
                    <label className="relative block cursor-pointer">
                      <input type="radio" name="radio-buttons" className="peer sr-only" defaultChecked id="moderately_aggressive"/>
                      <div className="flex items-center bg-white text-sm font-medium text-slate-800 p-4 rounded border border-slate-200 hover:border-slate-300 shadow-sm duration-150 ease-in-out">
                        <span>Moderately Aggressive</span>
                      </div>
                      <div className="absolute inset-0 border-2 border-transparent peer-checked:border-[#1ddcdc] rounded pointer-events-none" aria-hidden="true"></div>
                    </label>
                    <label className="relative block cursor-pointer">
                      <input type="radio" name="radio-buttons" className="peer sr-only" defaultChecked id="moderate"/>
                      <div className="flex items-center bg-white text-sm font-medium text-slate-800 p-4 rounded border border-slate-200 hover:border-slate-300 shadow-sm duration-150 ease-in-out">
                        <span>Moderate</span>
                      </div>
                      <div className="absolute inset-0 border-2 border-transparent peer-checked:border-[#1ddcdc] rounded pointer-events-none" aria-hidden="true"></div>
                    </label>
                    <label className="relative block cursor-pointer">
                      <input type="radio" name="radio-buttons" className="peer sr-only" defaultChecked id="moderately_conservative"/>
                      <div className="flex items-center bg-white text-sm font-medium text-slate-800 p-4 rounded border border-slate-200 hover:border-slate-300 shadow-sm duration-150 ease-in-out">
                        <span>Moderately Conservative</span>
                      </div>
                      <div className="absolute inset-0 border-2 border-transparent peer-checked:border-[#1ddcdc] rounded pointer-events-none" aria-hidden="true"></div>
                    </label>
                    <label className="relative block cursor-pointer">
                      <input type="radio" name="radio-buttons" className="peer sr-only" defaultChecked id="conservative"/>
                      <div className="flex items-center bg-white text-sm font-medium text-slate-800 p-4 rounded border border-slate-200 hover:border-slate-300 shadow-sm duration-150 ease-in-out">
                        <span>Conservative</span>
                      </div>
                      <div className="absolute inset-0 border-2 border-transparent peer-checked:border-[#1ddcdc] rounded pointer-events-none" aria-hidden="true"></div>
                    </label>
                    <label className="relative block cursor-pointer">
                      <input type="radio" name="radio-buttons" className="peer sr-only" defaultChecked id="ultra_conservative"/>
                      <div className="flex items-center bg-white text-sm font-medium text-slate-800 p-4 rounded border border-slate-200 hover:border-slate-300 shadow-sm duration-150 ease-in-out">
                        <span>Ultra Conservative</span>
                      </div>
                      <div className="absolute inset-0 border-2 border-transparent peer-checked:border-[#1ddcdc] rounded pointer-events-none" aria-hidden="true"></div>
                    </label>
                  </div>
                  <div className="flex items-center justify-between">
                    <a className="btn bg-[#1ddccc] hover:bg-[#1ddcdccc] hover:cursor-pointer text-white ml-auto rounded-full p-2 pl-4 pr-4" onClick={handleClick}>Next Step -&gt;</a>
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

export default Onboarding01;
