import React, { useEffect, useState } from "react";
import { useRouter } from "next/router";

import { graphParser, topTickerParser } from "../lib/parser";

import Navbar from "../components/Navbar";
import FintechIntro from "../components/partials/FintechIntro";
import FintechCard01 from "../components/partials/FintechCard01";
import FintechCard02 from "../components/partials/FintechCard02";
import FintechCard05 from "../components/partials/FintechCard05";
import FintechCard10 from "../components/partials/FintechCard10";

export default function Dashboard() {
  const url = "http://88db-129-110-241-55.ngrok.io/"

  const [data, setData] = useState<
    (
      | (string | number[])[]
      | (string | number[])[][][]
      | {
          bonds_and_notes: number;
          commodities: number;
          realEstate: number;
          stocks: number;
        }
      | { moderate: number }
    )[]
  >();
  const [top, setTop] = useState<string[][]>();

  let router = useRouter();

  useEffect(() => {
    let obj = localStorage.getItem("obj");
    if (!obj) {
      router.push("/");
    }

    fetch(`${url}/analytics`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: obj,
    })
    .then((res) => res.json())
    .then((res) => {
      console.log(res)
      setData(graphParser(res))
    }).catch((error) =>{
      console.log(error)
    })
    fetch(`${url}/top-holdings`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        category: JSON.parse(localStorage.getItem("obj") || "{}")["balance"],
      }),
    })
      .then((res) => res.json())
      .then((res) => {
        console.log(res);
        setTop(topTickerParser(res));
      });
  }, []);

  return (
    <>
      <div className="relative">
        <Navbar />
      </div>

      {data && top && 
        <div className="flex h-[90%] overflow-hidden">
          <div className="relative flex flex-col flex-1 overflow-y-auto overflow-x-hidden">
            <main>
              <div className="px-4 sm:px-6 lg:px-8 py-8 w-full max-w-9xl mx-auto">
                <div className="sm:flex sm:justify-between sm:items-center mb-5">
                  <div className="mb-4 sm:mb-0">
                    <h1 className="text-2xl md:text-3xl text-slate-800 font-bold">
                      Dashboard
                    </h1>
                  </div>

                  <div className="grid grid-flow-col sm:auto-cols-max justify-start sm:justify-end gap-2"></div>
                </div>

                <div className="flex flex-col gap-6">
                  <FintechIntro
                    strategy={
                      JSON.parse(localStorage.getItem("obj") || "{}")["balance"]
                    }
                    rating={
                      data[2][JSON.parse(localStorage.getItem("obj") || "{}")["balance"]]
                    }
                  />

                  <div className="flex flex-row w-[100%] gap-5">
                    <div className="w-[100%]">
                      <FintechCard02 data={data[3][1]} ticker={data[3][0]} rating={data[2][JSON.parse(localStorage.getItem("obj") || "{}")["balance"]]} />
                    </div>
                  </div>

                  {/* News */}
                  {/* <div className="flex flex-row w-[100%] h-[auto] gap-5 mb-5">
                    <div className="basis-1/4 text-black">
                      <FintechCard11
                        category={data[4][0].author}
                        value={data[4][0].title}
                      />
                    </div>
                    <div className="basis-1/4">
                      <FintechCard11
                        category={data[4][1].author}
                        value={data[4][1].title}
                      />
                    </div>
                    <div className="basis-1/4">
                      <FintechCard11
                        category={data[4][2].author}
                        value={data[4][2].title}
                      />
                    </div>
                    <div className="basis-1/4">
                      <FintechCard11
                        category={data[4][3].author}
                        value={data[4][3].title}
                      />
                    </div>
                  </div> */}

                  {data[0]?.map((key) => {
                    if (key[1] !== undefined) {
                      return (
                        <div className="flex flex-row w-[100%] gap-5">
                          <div className="basis-1/2 w-[50%]">
                            <FintechCard01
                              data={key[0][1]}
                              ticker={key[0][0]}
                            />
                          </div>
                          <div className="basis-1/2 w-[50%]">
                            <FintechCard01
                              data={key[1][1]}
                              ticker={key[1][0]}
                            />
                          </div>
                        </div>
                      );
                    } else {
                      return (
                        <div className="flex flex-row w-[100%] gap-5">
                          <div className="w-[100%]">
                            <FintechCard01
                              data={key[0][1]}
                              ticker={key[0][0]}
                            />
                          </div>
                        </div>
                      );
                    }
                  })}

                  <FintechCard05 data={top} />

                  <div className="flex flex-row w-[100%] h-24 gap-5">
                    <div className="basis-1/4">
                      <FintechCard10
                        category={"Bonds & notes"}
                        value={
                          Math.ceil(2000*Math.random())
                        }
                      />
                    </div>
                    <div className="basis-1/4">
                      <FintechCard10
                        category={"Commodities"}
                        value={
                          Math.ceil(2000*Math.random())
                        }
                      />
                    </div>
                    <div className="basis-1/4">
                      <FintechCard10
                        category={"Real & Estate"}
                        value={
                          Math.ceil(2000*Math.random())
                        }
                      />
                    </div>
                    <div className="basis-1/4">
                      <FintechCard10
                        category={"Stocks"}
                        value={
                          Math.ceil(2000*Math.random())
                        }
                      />
                    </div>
                  </div>



                </div>
              </div>
            </main>
          </div>
        </div>
      }
    </>
  );
}
