import React from 'react';

function FintechCard11({category, value}) {

  return (
    <div className="flex flex-col col-span-full sm:col-span-6 xl:col-span-3 bg-white shadow-lg rounded-sm border border-slate-200 h-[100%]">
      <div className="px-5 pt-5">
        <header>
          <h3 className="text-xl font-semibold text-[#1ddcdc] uppercase mb-1">
            <span className="text-[#1ddcdc]">{category}</span>
          </h3>
          <div className="text-lg font-semibold text-[#777777] mb-1">{value}</div>
        </header>
      </div>
    </div>
  );
}

export default FintechCard11;
