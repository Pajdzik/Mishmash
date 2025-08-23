let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'

let lines_to_array lines =
  Array.of_list (List.map (fun s -> String.to_seq s |> Array.of_seq) lines)

module Tuple4Set = Set.Make (struct
  type t = int * int * int * int
  let compare (x1, y1, z1, w1) (x2, y2, z2, w2) =
    let c = compare x1 x2 in
    if c <> 0 then c
    else
      let c = compare y1 y2 in
      if c <> 0 then c
      else
        let c = compare z1 z2 in
        if c <> 0 then c else compare w1 w2
end)
  
let print_tuple4_set set =
  Tuple4Set.iter (fun (i, j, di, dj) ->
    Printf.printf "(%d, %d, %d, %d)\n" i j di dj
  ) set

let process_part1 (arr : char array array) =
  let m = Array.length arr in
  let n = Array.length (Array.get arr 0) in

  let rec find_starting_point arr i =
    match i with
    | i when i >= m -> failwith "Start not found"
    | i -> (
        let row = Array.get arr i in
        let maybe_j = Array.find_index (fun el -> el == '^') row in
        match maybe_j with
        | Some j ->
            Array.set (Array.get arr i) j '.';
            (i, j)
        | None -> find_starting_point arr (i + 1))
  in

  let change_direction di dj =
    match (di, dj) with
    | -1, 0 -> (0, 1)
    | 0, 1 -> (1, 0)
    | 1, 0 -> (0, -1)
    | 0, -1 -> (-1, 0)
    | _ -> failwith "What kind of direction is that"
  in

  let find_matching_coords set pos =
    let i, j, di, dj = pos in
    let next_dir = change_direction di dj in
    (Tuple4Set.mem (i, j, fst next_dir, snd next_dir) set || Tuple4Set.mem pos set)
  in

  let rec traverse arr i j di dj seen traps =
    (* print_string (string_of_int path_length ^ ":\t" ^ string_of_int (i + 1) ^ ", " ^ string_of_int (j + 1)); *)
    match (i, j) with
    | i, j when i < 0 || j < 0 -> traps
    | i, j when i >= m || j >= n -> traps
    | _ ->
        let el = Array.get (Array.get arr i) j in

        (* print_endline (" " ^ String.make 1 el); *)
        let ni, nj, ndi, ndj, seen, ntraps =
          match el with
          | '#' ->
              let ndi, ndj = change_direction di dj in
              (i - di, j - dj, ndi, ndj, seen, traps)
          | c ->
              (* print_tuple4_set seen; *)
              let already_seen = find_matching_coords seen (i, j, di, dj) in
              let ntraps = match already_seen with
              | true -> traps + 1
              | false -> traps in
              let new_seen = Tuple4Set.add (i, j, di, dj) seen in
              (i + di, j + dj, di, dj, new_seen, ntraps)
        in

        traverse arr ni nj ndi ndj seen ntraps
  in

  let start_i, start_j = find_starting_point arr 0 in
  let seen = Tuple4Set.empty in
  traverse arr start_i start_j (-1) 0 seen 0

let () =
  read_lines "day6.test.txt" |> lines_to_array |> process_part1 |> print_int;
  print_newline ()
