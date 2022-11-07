# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end

def merge_two_lists(list1, list2)
    dummy = ListNode.new
    current = dummy

    while list1 or list2 do
        if list1 and list2 then
            if list1.val < list2.val then
                current.next = list1
                current = list1
                list1 = list1.next
            else
                current.next = list2
                current = list2
                list2 = list2.next
            end
        elsif list1 then
            current.next = list1
            current = list1
            list1 = list1.next
        elsif list2 then
            current.next = list2
            current = list2
            list2 = list2.next
        end
    end

    return dummy.next
end