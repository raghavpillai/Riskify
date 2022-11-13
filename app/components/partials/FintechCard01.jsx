import React from 'react';
import LineChart from '../charts/LineChart05';

// Import utilities
import { tailwindConfig, hexToRGB } from '../../utils/Utils';
import {labels} from '../../lib/exports'

function FintechCard01({data, ticker}) {

  const chartData = {
    labels: labels,
    datasets: [
      {
        label: 'Mosaic Portfolio',
        data: data,
        borderColor: 'rgba(29, 220, 220)',
        fill: true,
        backgroundColor: 'rgba(29, 220, 220, 0.08)',
        borderWidth: 2,
        tension: 0,
        pointRadius: 0,
        pointHoverRadius: 3,
        pointBackgroundColor: 'rgba(29, 220, 220, 0.08)',
        clip: 20,
      },
    ],
  };

  return (
    <div className="flex flex-col col-span-full xl:col-span-8 bg-white shadow-lg rounded-sm border border-slate-200">
      <header className="px-5 py-4 border-b border-slate-100 flex items-center">
        <h2 className="font-semibold text-slate-800">Value at Risk Chart</h2>
      </header>
      {/* Chart built with Chart.js 3 */}
      {/* Change the height attribute to adjust the chart height */}
      <LineChart data={chartData} width={800} height={300} ticker={(""+ticker).toUpperCase()}/>
    </div>
  );
}

export default FintechCard01;
