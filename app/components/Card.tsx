import React from 'react';
import { useState, useEffect } from 'react';

interface Props {
    className: string;
    data: Object;
}

interface Object {
    title: string,
    data: string,
}

export default function Card(props: Props) {

    const [state, setState] = useState(false)

    const handleClick = () =>{
        setState(!state)
    }

    return (
        <div className={props.className}>

            {!state &&
            <div className='flex flex-row bg-[#ffffffc0] rounded-lg border-2 p-5 card h-[100%]' onClick={handleClick}>
                <div className='text-5xl w-[100%] self-center font-bold text-center'>
                    {props.data.title}
                </div>
            </div>}

            {state && 
            <div className='flex flex-row bg-[#ffffffc0] rounded-lg border-2 p-5 card h-[100%]' onClick={handleClick}>
                <div className='flex flex-col h-[100%] justify-center self-center items-center'>
                    <div className='font-semibold self-center text-center'>
                        {props.data.data}
                    </div>
                </div> 
            </div>}
        </div>
    )
}