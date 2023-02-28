#!/usr/bin/env ruby

# @param {String[]} names
# @param {Integer[]} heights
# @return {String[]}
def sort_people(names, heights)
    names.zip(heights).sort_by {|a| -a[1]}.map {|a| a[0]}
end