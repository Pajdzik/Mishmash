let read_lines file_name =
  In_channel.with_open_bin file_name In_channel.input_all
  |> String.split_on_char '\n'
  |> List.filter (fun x -> x <> "")

let print_string_list arr =
  List.iter
    (fun x ->
      print_string x;
      print_string ", ")
    arr;

  print_newline ()

let print_int_list arr =
  List.iter
    (fun x ->
      print_int x;
      print_string ", ")
    arr;

  print_newline ()

let pow x y =
  let rec aux acc x y = if y = 0 then acc else aux (acc * x) x (y - 1) in
  aux 1 x y

let process lines =
  let parse_program_line line =
    let parts = String.split_on_char ' ' line in
    match parts with
    | [ label; codes ] ->
        String.split_on_char ',' codes
        |> List.map int_of_string |> Array.of_list
    | _ -> failwith "Unpexpected program line"
  in
  let parse_register_value line =
    let parts = String.split_on_char ' ' line in
    match parts with
    | [ _; _; value ] -> int_of_string value
    | s ->
        print_string_list s;
        failwith "Unpexpected register value"
  in
  let parse = function
    | [ reg_a_str; reg_b_str; reg_c_str; program_str ] ->
        let reg_a = parse_register_value reg_a_str in
        let reg_b = parse_register_value reg_b_str in
        let reg_c = parse_register_value reg_c_str in
        let program = parse_program_line program_str in
        (reg_a, reg_b, reg_c, program)
    | s ->
        print_string_list s;
        failwith "Unpexpected number of lines"
  in

  let rec run_program acc reg_a reg_b reg_c codes index =
    let get_operand codes index =
      if index >= Array.length codes then (0, index)
      else (codes.(index), index + 1)
    in

    let get_combo_operand codes index =
      if index >= Array.length codes then (0, index)
      else
        let operand =
          match codes.(index) with
          | (0 | 1 | 2 | 3) as combo -> combo
          | 4 -> reg_a
          | 5 -> reg_b
          | 6 -> reg_c
          | _ -> failwith "Invalid combo operand"
        in
        (operand, index + 1)
    in

    if index >= Array.length codes then acc
    else
      let code = codes.(index) in
      let _  =
        match code with
        | 0 -> "DIV_A"
        | 1 -> "XOR_B_OP"
        | 2 -> "MOV_MOD_8"
        | 3 -> "JMP_IF_NOT_ZERO"
        | 4 -> "XOR_B_C"
        | 5 -> "PRINT"
        | 6 -> "DIV_B"
        | 7 -> "DIV_C"
        | _ -> failwith "Invalid code"
      in
      (* print_endline
        (Printf.sprintf "ins: %s\top: %d\tA: %d B: %d C: %d" op codes.(index + 1) reg_a reg_b reg_c); *)
      match code with
      | 0 ->
          let operand, next_index = get_combo_operand codes (index + 1) in
          let denominator = pow 2 operand in
          let reg_a' = reg_a / denominator in
          run_program acc reg_a' reg_b reg_c codes next_index
      | 1 ->
          let operand, next_index = get_operand codes (index + 1) in
          let reg_b' = reg_b lxor operand in
          run_program acc reg_a reg_b' reg_c codes next_index
      | 2 ->
          let operand, next_index = get_combo_operand codes (index + 1) in
          let reg_b' = operand mod 8 in
          run_program acc reg_a reg_b' reg_c codes next_index
      | 3 ->
          let next_index, _ =
            if reg_a = 0 then (index + 1, 0) else get_operand codes (index + 1)
          in
          run_program acc reg_a reg_b reg_c codes next_index
      | 4 ->
          let reg_b' = reg_b lxor reg_c in
          run_program acc reg_a reg_b' reg_c codes (index + 2)
      | 5 ->
          let operand, next_index = get_combo_operand codes (index + 1) in
          (* print_string (Printf.sprintf "[%d]\n" (operand mod 8)); *)
          run_program ((operand mod 8) :: acc) reg_a reg_b reg_c codes
            next_index
      | 6 ->
          let operand, next_index = get_combo_operand codes (index + 1) in
          let denominator = pow 2 operand in
          let reg_b' = reg_a / denominator in
          run_program acc reg_a reg_b' reg_c codes next_index
      | 7 ->
          let operand, next_index = get_combo_operand codes (index + 1) in
          let denominator = pow 2 operand in
          let reg_c' = reg_a / denominator in
          run_program acc reg_a reg_b reg_c' codes next_index
      | _ -> failwith "Invalid code"
  in

  let reg_a, reg_b, reg_c, program = parse lines in
  (* run_program [] reg_a reg_b reg_c program 0; *)

  let rec loop reg_a =
    (* print_endline (Printf.sprintf "Register A: %d" reg_a); *)
    let acc = run_program [] reg_a 0 0 program 0 in
    let result = List.rev acc in
    let concat_result =
      List.fold_left (fun acc x -> acc ^ string_of_int x) "" result
    in
    (* print_endline concat_result; *)
    if concat_result = "2411754414035530" then print_endline ("Found it! " ^ (string_of_int reg_a))
    else loop (reg_a + 1)
  in
  loop 137441213;
  0

let () =
  read_lines "day17.txt" |> process |> print_int;
  print_newline ()
