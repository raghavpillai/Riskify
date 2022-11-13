import Head from 'next/head'
import Image from 'next/image'
import SignInSide from './signup'
import Navbar from '../components/Navbar'
import Card from '../components/Card'
import sc1 from '../public/form-preview.png'

export default function Home() {
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
            <ul className='typewriter-elements pl-3'>
                <li><span>build wealth</span></li>
                <li><span>invest smarter</span></li>
                <li><span>create a bright future</span></li>
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
      
      <div className='flex flex-col w-[95%] h-[auto] bg-[#dfdfdf] rounded p-10 ml-[2.5%] gap-5'>
        <div className='flex flex-row w-[100%] gap-5'>
          <Image className="h-[100%] basis-1/2 rounded float-left"src={sc1} alt=""/>
          <div className='flex flex-col self-center'>
            <div className='text-right text-[#1ddcdc] font-bold text-4xl'>Ease of Use</div>
            <div className='basis-1/2 text-right self-center text-[#777777] font-semibold'>Intuitive and user friendly user interface designed for all people. Made by people, for the people.</div>
          </div>
          
        </div>
        <div className='flex flex-row w-[100%] gap-5'>
          <div className='flex flex-col self-center'>
            <div className='text-left text-[#1ddcdc] font-bold text-4xl'>Win Your Future Today</div>
            <div className='text-left self-center text-[#777777] font-semibold'>Get financial advice through our algorithm's risk assesments and useful metrics. Start your path to financial freedom through smart investments and risk analysis.</div>
          </div>
          <Image className="h-[100%] basis-1/2 rounded float-right"src={sc1} alt=""/>
        </div>
        
      </div>
      
  
      {/* About Section */}
      <div className="snap-center h-[25%] mt-[20%] relative">
        <div className='p-10 pb-0 text-7xl font-bold text-black text-center'>
          About
        </div>
        
        <div className='flex md:flex-row md:h-[100%] mt-10 flex-col gap-5 p-10 w-screen justify-center'>
          <Card className={'basis-1/2 h-[100%]'} 
            data={
              {
                title:"What do we do?",
                data: "We take care of find the the risk rating of your portfolio, so that you can manage your money and assets wisely"
              }} 
          />
          <Card className={'basis-1/2 h-[100%]'} 
            data={
              {
                title:"Who is this for?",
                data: "Investors everywhere in the United States of America benefit from the metrics calculated through this application to grow their portfolios"
              }} 
          />
        </div>
        <div className="h-[5%] mt-[10%]"id="about"></div>
      </div>
      

    </div>

  )
}
