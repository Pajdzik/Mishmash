let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char ','

let process_part1 (sequences : string list) =
  let rec hash_value value index sequence =
    match index with
    | i when String.length sequence <= i -> value
    | i ->
        let c = String.get sequence i in
        let ascii_code = Char.code c in
        let new_value = (value + ascii_code) * 17 mod 256 in
        hash_value new_value (index + 1) sequence
  in

  sequences |> List.map (hash_value 0 0) |> List.fold_left ( + ) 0

let () = read_lines "day15.txt" |> process_part1 |> print_int
