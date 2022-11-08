class MyQueue
    def initialize()
        @stack = []
        @reversed = []
    end

=begin
    :type x: Integer
    :rtype: Void
=end
    def push(x)
        @stack << x
    end

=begin
    :rtype: Integer
=end
    def pop()
        fill_reverse()
        ret = @reverse.pop()
        reverse_back()
        return ret
    end

=begin
    :rtype: Integer
=end
    def peek()
        fill_reverse()
        ret = @reverse.last
        return ret
    end


=begin
    :rtype: Boolean
=end
    def empty()
        @stack.empty?
    end

    def fill_reverse()
        @reverse = []
        @stack.reverse_each { |x| @reverse << x}
    end

    def reverse_back()
        @stack = []
        @reverse.reverse_each { |x| @stack << x }
    end
end

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue.new()
obj.push(1)
puts obj.pop()
puts obj.empty()