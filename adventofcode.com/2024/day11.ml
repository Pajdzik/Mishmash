let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'
  |> List.filter (fun x -> x <> "")
  |> List.hd |> String.split_on_char ' '
  |> List.map (fun c -> int_of_string c)

(*

0 -> 1
digits(n) == even -> [l(n), r(n)]
n -> n * 2024
*)

(*
0 -> 1 -> 2024 -> 20 24 -> 2 0 2 4 -> 4048 1 4048 8096 -> 40 48 2024 40 48 80 96 
-> 4    0    4     8  20  24    4 0    4     8     8 0     9     6 
-> 8096 1 8096 16192 2 0 2 4 8096 1 8096 16192 16192 1 18216 12144
*)

(*
 0 -> 1
 1 -> 2024  -> 20 24 -> 2 0 2 4
 2 -> 4048 -> 40 48 -> 4 0 4 8
 3 -> 6072 -> 60 72 -> 6 0 7 2
 4 -> 8096 -> 80 96 -> 8 0 9 6
 5 -> 10120 -> 20482880 -> 2048 2880 -> 20 48 28 80 -> 2 0 4 8 2 8 8 0
 6 -> 12144 -> 24579456 -> 2457 9456 -> 24 57 94 56 -> 2 4 5 7 9 4 5 6
 7 -> 14168 -> 28676032 -> 2867 6032 -> 28 67 60 32 -> 2 8 6 7 6 0 3 2
 8 -> 16192 -> 32772608 -> 3277 2608 -> 32 77 26 08 -> 3 2 7 7 2 6 0 8
 9 -> 18216 -> 36869184 -> 3686 9184 -> 36 86 91 84 -> 3 6 8 6 9 1 8 4
 10 -> 1 0
*)

let process line =
  let process_stone = function
    | 0 -> [ 1 ]
    | n when n >= 10 && n <= 99 -> [ n / 10; n mod 10 ]
    | n when n >= 1000 && n <= 9999 -> [ n / 100; n mod 100 ]
    | n when n >= 100_000 && n <= 999_999 -> [ n / 1000; n mod 1000 ]
    | n when n >= 1000_0000 && n <= 9999_9999 -> [ n / 10000; n mod 10000 ]
    | n when n >= 10000_00000 && n <= 99999_99999 -> [ n / 100000; n mod 100000 ]
    | n when n >= 100000_000000 && n <= 999999_999999 -> [ n / 1000000; n mod 1000000 ]
    | n -> [ n * 2024 ]
  in

  let rec count_stones iter stones =
    match iter with
    | 0 -> List.length stones
    | _ ->
        let new_stones = List.map process_stone stones |> List.flatten in
        count_stones (iter - 1) new_stones
  in

  count_stones 25 line

let () =
  read_lines "day11.txt" |> process |> print_int;
  print_newline ()
