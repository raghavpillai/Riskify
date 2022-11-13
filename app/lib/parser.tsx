import dump from "./dump.json";
import dump2 from "./dump2.json";

export function graphParser(response_data) {
  const ind_graphs = response_data.future_points.ind_graphs;
  let tickers = [];
  let res = [];
  let ticker: string;

  for (ticker in ind_graphs) {
    tickers.push([ticker, ind_graphs[ticker as keyof typeof ind_graphs]]);
  }

  for (let i = 0; i < tickers.length; i += 2) {
    res.push([tickers[i], tickers[i + 1]]);
  }

  return [
    res,
    response_data.balancing,
    response_data.risk,
    ["Total Graph", response_data.future_points.total_graph],
  ];
}

export function topTickerParser(response_data) {
  return response_data;
}
