from gasp import *

begin_graphics()

Line((300,300), (200,200))

Circle((300,300), 50)

Circle((200,200), 50)

Box((300,300), 80, 30)
update_when("key_pressed")
end_graphics()
