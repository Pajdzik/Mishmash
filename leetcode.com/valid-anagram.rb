# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)
    return false if s.length != t.length

    s_map, t_map = {}, {}
    
    s.each_char.with_index do |c, i|
        s_val = s_map[s[i]]
        t_val = t_map[t[i]]
        s_map[s[i]] = s_val.nil? ? 1 : s_val + 1
        t_map[t[i]] = t_val.nil? ? 1 : t_val + 1
    end

    s.each_char do |c|
        return false if s_map[c] != t_map[c]
    end

    return true
end