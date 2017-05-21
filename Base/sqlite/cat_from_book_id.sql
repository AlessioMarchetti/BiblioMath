select id, name, id_parent from categories
    left join cat_ref on categories.id == cat_ref.id_cat
    where cat_ref.id_book == {id_book};