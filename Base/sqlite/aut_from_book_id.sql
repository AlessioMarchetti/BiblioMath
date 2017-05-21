select id, name from authors
    left join aut_ref on authors.id == aut_ref.id_aut
    where aut_ref.id_book == {id_book};