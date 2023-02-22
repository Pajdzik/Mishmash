#!/usr/bin/env ruby

class MyStack
    def initialize()
        @queue = []
    end

    def push(x)
        @queue.append(x)
    end

    def pop()
        reverse
        ret = @queue.shift
        reverse
        ret
    end

    def top()
        reverse
        ret = @queue[0]
        reverse
        ret
    end

    def reverse()
        temp_queue = []
        while !@queue.empty?
            temp_queue.append(@queue.pop)
        end
        @queue = temp_queue
    end

    def empty()
        @queue.empty?
    end
end

# Your MyStack object will be instantiated and called as such:
obj = MyStack.new()
obj.push(1)
obj.push(2)
puts obj.top()
puts obj.pop()
puts obj.empty()