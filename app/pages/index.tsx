import Head from 'next/head'
import Image from 'next/image'
import SignInSide from './signup'
import Navbar from '../components/Navbar'
import Card from '../components/Card'
import formPrev from '../public/form-preview.png'
import dashPrev from '../public/dash-preview.png'
import { useEffect } from 'react'

export default function Home() {
  useEffect(() => {
    if(JSON.parse(localStorage.getItem('obj') || '{}') != '{}'){
      localStorage.clear()
    }
  },[])

  return (
    <div className='w-screen h-screen overflow-scroll scroll-smooth snap-y snap-center'>
      <Navbar />

      <div className='flex flex-col self-center text-center h-[10%] mt-[10%] p-5'>
        <div className='p-5 font-bold text-8xl text-left'>
          Risk Assesment <div className='text-[#1ddcdc]'>S i m p l i f i e d</div>
        </div>
      </div>

      <div className='p-5 flex flex-row text-black font-bold text-5xl h-[70%] justify-items-center gap-56'>
        
        {/* Typewriter */}
        <div className='self-center'>
          <div className='typewriter justify-center p-5 basis-3/4'>
            <div className='typewriter-prefix'>Together let's </div>
            <ul className='typewriter-elements pl-3 text-[#09c7c7]'>
                <li className='leading-none'><span className='w-full'>build wealth</span></li>
                <li className='leading-none'><span className='w-full'>invest smarter</span></li>
                <li className='leading-none'><span className='w-full'>create a bright future</span></li>
            </ul>
          </div>
        </div>

        {/* Button */}
        <div className='basis-1/4 flex flex-col self-center text-center gap-10 mt-[-20%]'>
          <div className='font-bold text-3xl self-center'>
            Get a risk assessment now
          </div>
          <a href="/form-01"className='button border-2 text-lg w-[auto] rounded-full text-[#efefef] bg-[#ffffff] p-5'> take me there </a>
        </div>

      </div>
      
      <div className='flex flex-col w-[95%] h-[auto] bg-[#dfdfdf] rounded p-10 ml-[2.5%] gap-5 shadow-lg'>
        <div className='flex flex-row w-[100%] gap-5'>
          <Image className="drop-shadow-lg h-[100%] w-[10%] lg:w-[50%] basis-1/2 rounded float-left"src={formPrev} alt=""/>
          <div className='flex flex-col self-center'>
            <div className='text-right text-[#1ddcdc] font-bold text-4xl'>Ease of Use</div>
            <div className='basis-1/2 text-right self-center text-[#777777] font-semibold'>
              Intuitive and user friendly user interface designed for all people. Made by people, for the people.
            </div>
          </div>
          
        </div>
        <div className='flex flex-row w-[100%] gap-5'>
          <div className='flex flex-col self-center'>
            <div className='text-left text-[#1ddcdc] font-bold text-4xl'>Win Your Future Today</div>
            <div className='text-left self-center text-[#777777] font-semibold'>
              Get financial data and useful metrics through our risk assesment algorithms. 
              Start your path to financial freedom through smart investments and risk analysis.
              Sit back, <span className="text-[#09c7c7] self-center">R E L A X</span> , and let Riskify handle the complicated stuff.
            </div>
          </div>
          <Image className="drop-shadow-lg h-[100%] w-[50%] basis-1/2 rounded float-right"src={dashPrev} alt=""/>
        </div>
        
      </div>
      
  
      {/* About Section */}
      <div className='p-10 pb-0 text-7xl font-bold text-black text-center mt-[20%]'>
          About
      </div>
      <div className="flex flex-col snap-center h-[25%] mb-20" id="about">
        <div className='flex md:flex-row md:h-[100%] mt-10 flex-col gap-5 p-10 w-screen justify-center'>
          <Card className={'basis-1/2 h-[100%]'} 
            data={
              {
                title:"What do we do?",
                data: "We take care of find the the risk rating of your portfolio, so that you" +
                "can manage your money and assets wisely"
              }} 
          />
          <Card className={'basis-1/2 h-[100%]'} 
            data={
              {
                title:"Who is this for?",
                data: "Investors everywhere in the United States of America benefit from"+ 
                "the metrics calculated through this application to grow their portfolios"
              }} 
          />
        </div>
        <div className='flex md:flex-row md:h-[100%] -mt-14 flex-col gap-5 p-10 w-screen justify-center'>
          <Card className={'basis-1/2 h-[100%]'} 
            data={
              {
                title:"Why is this important?",
                data: "As a group we believe that managing assets and money is not only a way to create wealth," +
                "but also a way to create opportunities and open many doors. Good financial health is an important"+
                "part of life which is often neglected. We aim to solve this."
              }} 
          />
          <Card className={'basis-1/2 h-[100%]'} 
            data={
              {
                title:"Credits",
                data: "Kanish Garg - Backend, Raghav Pillai - Backend, Rishabh Vemparala - Frontend, Ryan Donaldson - Backend"
              }} 
          />
        </div>
        <div id="about"></div>
        <div className='w-screen h-[100%] text-center text-[#777777] font-semibold'>Riskify 2022</div>
      </div>
      
      
      

    </div>

  )
}
