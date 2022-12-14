import { AiOutlineMenu } from 'react-icons/ai';
import React from 'react';
import Image from 'next/image'
import { useState, useEffect } from 'react';
import logo from '../public/riskify-logo.png'

export default function Navbar() {

    const [state, setState] = useState(false)

    const handleClick = () => {
        setState(!state)
    }

    return (
        <>
        <div className="flex flex-row bg-[#555555] w-screen h-[10%] p-5 lg:text-3xl md:text-2xl sm:text-xl overflow-hidden drop-shadow">
            <h1 className="flex flex-row basis-3/4 font-bold text-white pl-5 self-center gap-5">
                <a className="self-center h-full w-[5%]"href="/">
                    <div className="self-center">
                        <Image src={logo} alt=""/>
                    </div>
                </a>
                <a className='self-center' href="/">Riskify</a>
            </h1>
            <div className="flex flex-row basis-1/4 self-center pr-5 gap-5 lg:text-xl md:text-lg sm:text-md">
                <a className="basis-1/2" href="/form-01">
                    <h1 className="text-center font-semibold text-white border-2 border-[#777777] self-center rounded p-2 navitem">
                        find risk
                    </h1>
                </a>
                <a className="basis-1/2" href="/#about">
                    <h1 className="text-center font-semibold text-white border-2 border-[#777777] self-center rounded p-2 navitem">
                        about
                    </h1>
                </a>
            </div>
        </div>
        </>
    )
}