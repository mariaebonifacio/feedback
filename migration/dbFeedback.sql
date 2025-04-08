create database db_feedback;
use db_feedback;

create table tb_comentarios(

	nome varchar (150) not null,
    data_hora datetime not null,
    comentario text not null,
    cod_comentario int auto_increment primary key

);

select * from tb_comentarios;

UPDATE tb_coemntarios
SET curtidas = curtidas + 1
WHERE cod_comentario = 56;

set sql_safe_update = 0;

-- MATERIALIZE
-- <div class="result2">

--             <table>
--                 <thead>
--                     <td>
--                         LOGIN
--                     </td>
--                     <td>
--                         NOME
--                     </td>
--                     <td>
--                         SENHA
--                     </td>
--                 </thead>

--                 {% for usuario in usuarios %}
--                 <div class="mensagem">
--                     <tr>
--                         <td>
--                             {{usuario.login}}
--                         </td>
--                         <td>
--                             {{usuario.nome}}
--                         </td>
--                         <td>
--                             {{usuario.senha}}
--                         </td>
                       
--                     </tr>
--                 </div>
--                 {% endfor %}
--         </table>
--   </div>