# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    min_price = prices[0]
    max_profit = 0
    prices.each do |price| 
        profit = price - min_price
        max_profit = profit if profit > max_profit 
        min_price = price if price < min_price
    end

    return max_profit
end