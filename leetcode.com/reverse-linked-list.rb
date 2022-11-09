# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end
# @param {ListNode} head
# @return {ListNode}
def reverse_list(head)
    return head if head&.next.nil?

    previous = head
    current = head.next
    nxt = current&.next

    head.next = nil
    
    while !current.nil? do
        t_nxt = nxt.next if nxt
        nxt.next = current if nxt
        current.next = previous

        previous = current
        current = nxt
        nxt = t_nxt
    end

    return previous
end