# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

def hasCycle(head)
    slow = head
    fast = head&.next

    while !fast.nil? and !slow.nil? do
        return true if slow == fast

        slow = slow&.next
        fast = fast&.next&.next
    end

    return false
end


require 'set'

# @param {ListNode} head
# @return {Boolean}
def hasCycle_memory(head)
    cache = Set.new

    while !head.nil? do
        return true if cache.include?(head)

        cache << head
        head = head.next
    end
    
    return false
end