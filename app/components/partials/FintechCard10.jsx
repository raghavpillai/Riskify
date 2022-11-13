import React from 'react';

function FintechCard10({category, value}) {


  return (
    <div className="flex flex-col col-span-full sm:col-span-6 xl:col-span-3 bg-white shadow-lg rounded-sm border border-slate-200 h-[100%]">
      <div className="px-5 pt-5">
        <header>
          <h3 className="text-sm font-semibold text-slate-500 uppercase mb-1">
            <span className="text-slate-800">{category}</span>
          </h3>
          <div className="text-2xl font-bold text-[#38bf1d] mb-1">{value}</div>
        </header>
      </div>
    </div>
  );
}

export default FintechCard10;
