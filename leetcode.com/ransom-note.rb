# @param {String} ransom_note
# @param {String} magazine
# @return {Boolean}
def can_construct(ransom_note, magazine)
    magazine_counter = {}

    magazine.each_char { |c| magazine_counter[c] = magazine_counter.key?(c) ? magazine_counter[c] + 1 : 1 }
    
    ransom_note.each_char do |c|
        return false if !magazine_counter.key?(c) || magazine_counter[c] == 0
        magazine_counter[c] -= 1
    end

    return true
end