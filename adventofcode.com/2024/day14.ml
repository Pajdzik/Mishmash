let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'
  |> List.filter (fun x -> x <> "")

let get_robot_count_at_a_position r c positions =
  let result_array = Array.make_matrix r c 0 in

  List.iter
    (fun (x, y) ->
      let current = result_array.(y).(x) in
      result_array.(y).(x) <- current + 1)
    positions;

  result_array

let print_board board =
  Array.iter
    (fun row ->
      Array.iter
        (fun cell ->
          if cell > 0 then Printf.printf "%d" cell else print_string ".")
        row;
      print_newline ())
    board

type robot = { position : int * int; velocity : int * int }

let parse_line line =
  (* p=0,4 v=3,-3 *)
  Scanf.sscanf line "p=%d,%d v=%d,%d" (fun x y dx dy ->
      { position = (x, y); velocity = (dx, dy) })

let process r c lines =
  let calculate_final_position seconds robot =
    let x, y = robot.position in
    let dx, dy = robot.velocity in
    let nx = (x + (seconds * dx)) mod c in
    let ny = (y + (seconds * dy)) mod r in
    let nx' = if nx < 0 then nx + c else nx in
    let ny' = if ny < 0 then ny + r else ny in
    (nx', ny')
  in

  let should_count mr mc final_position =
    let x, y = final_position in
    x != mc && y != mr
  in

  let get_quadrant_count r c positions =
    let rec get_quadrant_count' result mr mc positions =
      match positions with
      | [] -> result
      | (x, y) :: rest ->
          let result' =
            match (x == mc, y == mr) with
            | false, false -> (
                match (x < mc, y < mr) with
                | true, true ->
                    result.(0).(0) <- result.(0).(0) + 1;
                    result
                | true, false ->
                    result.(0).(1) <- result.(0).(1) + 1;
                    result
                | false, true ->
                    result.(1).(0) <- result.(1).(0) + 1;
                    result
                | false, false ->
                    result.(1).(1) <- result.(1).(1) + 1;
                    result)
            | _ -> result
          in
          get_quadrant_count' result' mr mc rest
    in
    get_quadrant_count' (Array.make_matrix 2 2 0) (r / 2) (c / 2) positions
  in

  let input = List.map parse_line lines in

  (* 7138 *)
  for i = 2000 to 20000 do
    let positions = input |> List.map (calculate_final_position i) in
    let board = get_robot_count_at_a_position r c positions in
    print_board board;
    let s = read_line () in
    print_endline s;
    print_endline (Printf.sprintf "\n\nSecond: %d" i);

  done;

  0 


let () =
  read_lines "day14.txt" |> process 103 101 |> print_int;
  print_newline ()
