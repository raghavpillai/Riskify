import React from 'react';
import Image from 'next/image'

import UserImage from '../../public/riskify-logo.png'

function FintechIntro({ strategy, rating }) {

  function RenderRating(){
    const value = Math.ceil(parseFloat(rating)*100)
    if(value <= 33){
      return(
        <div className="self-center text-xl text-black font-bold">
          In The Overall Risk Rating is <span className='font-bold self-center text-xl text-[#56eb34]'>{value}</span>%
        </div>
      )
    }
    else if(value <= 66){
      return(
        <div className="self-center text-xl h-5 text-black font-bold">
          The Overall Risk Rating is <span className='font-bold self-center text-xl text-[#ebcd34]'>{value}</span>%
        </div>
      )
    }
    else {
      return(
        <div className="self-center text-xl h-5 text-black font-bold">
          The Overall Risk Rating is <span className='font-bold self-center text-xl text-[#eb4034]'>{value}</span>%
        </div>
      )
    }
  }


  return (
    <div className="flex flex-col col-span-full bg-white shadow-lg rounded-sm border border-slate-200">
      <div className="px-5 py-6">
        <div className="md:flex md:justify-between md:items-center">
          {/* Left side */}
          <div className="flex items-center mb-4 md:mb-0">
            {/* Avatar */}
            <div className="mr-4">
              <Image className="inline-flex rounded-full" src={UserImage} width="64" height="64" alt="" />
            </div>
            {/* User info */}
            <div>
              <div className="mb-2 self-center text-2xl gap-3">
                Analytics Dashboard For The <span className='font-bold'>{strategy}</span> Strategy
              </div>
              <RenderRating />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default FintechIntro;
