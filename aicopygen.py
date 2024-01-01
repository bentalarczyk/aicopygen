from openai import OpenAI
from tkinter import *
from PIL import Image, ImageTk
import urllib.request
import uuid
import os
from dotenv import load_dotenv
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

load_dotenv()

client = OpenAI(
    api_key= os.getenv("OPENAI_API_KEY"),
)

def show_frame(frame):
    frame.tkraise()

window = ttk.Window(themename='darkly')

window.title("AI Copy Generator")
window.state('zoomed')
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame0 = ttk.Frame(window)
frame0.columnconfigure((0,1,2,3,4), weight= 1, uniform='a')
frame0.rowconfigure((0,1,2,3), weight=1, uniform='a')
frame1 = ttk.Frame(window)
frame1.columnconfigure((0,1,2,3,4), weight= 1, uniform='a')
frame1.rowconfigure((0,1,2,3,4,5), weight=1, uniform='a')
frame2 = ttk.Frame(window)
frame2.columnconfigure((0,1,2,3,4), weight= 1, uniform='a')
frame2.rowconfigure((0,1,2,3,4), weight=1, uniform='a')
frame3 = ttk.Frame(window)
frame3.columnconfigure((0,1,2,3,4), weight= 1, uniform='a')
frame3.rowconfigure((0,1,2), weight=1, uniform='a')
frame3.rowconfigure(3, weight=10, uniform='a')
frame3.rowconfigure((4,5,6), weight=1, uniform='a')
frame4 = ttk.Frame(window)
frame4.columnconfigure((0,1,2,3,4), weight= 1, uniform='a')
frame4.rowconfigure((0,1), weight=1, uniform='a')
frame4.rowconfigure(2, weight=3, uniform='a')
frame4.rowconfigure((3,4), weight=1, uniform='a')
frame5 = ttk.Frame(window)
frame5.columnconfigure((0,1,2,3,4), weight= 1, uniform='a')
frame5.rowconfigure((0,1), weight=1, uniform='a')
frame5.rowconfigure(2, weight=10, uniform='a')
frame5.rowconfigure((3,4,5), weight=1, uniform='a')
frame6 = ttk.Frame(window)
frame6.columnconfigure((0,1,2), weight= 1, uniform='a')
frame6.rowconfigure((0,1,2), weight=1, uniform='a')

for frame in (frame0, frame1, frame2, frame3, frame4, frame5, frame6):
    frame.grid(row=0, column=0, sticky='nsew')

frame0_title = ttk.Label(frame0, text="Welcome to AI Copy Generator")
frame0_title.grid(row=1, column=2)

begin_btn = ttk.Button(frame0, text="Create Copy", command=lambda:show_frame(frame1), bootstyle=(LIGHT, OUTLINE))
begin_btn.grid(row=2, column=2, sticky="ew")

# previous_work = ttk.Button(frame0, text="Browse Previous Work", bootstyle=(LIGHT, OUTLINE))
# previous_work.grid(row=3, column=2, sticky="new")

main1_btn = ttk.Button(frame1, text="Main Menu", command=lambda:show_frame(frame0), bootstyle=(SECONDARY, OUTLINE))
main1_btn.grid(row=0, column=0, sticky="nw")

frame1_title = ttk.Label(frame1, text="Begin Prompt")
frame1_title.grid(row=1, column=2)

lbl = ttk.Label(frame1, text="Please enter a topic: ")
lbl.grid(row=2, column=2)

ent = Entry(frame1, width=70)
ent.grid(row=3, column=2)

def clear_topic():
    ent.delete(0,END)

delete_topic = ttk.Button(frame1, text="Clear topic", command=clear_topic, bootstyle=(LIGHT, OUTLINE))
delete_topic.grid(row=4, column=2)

frame1_btn = ttk.Button(frame1, text="Next", command=lambda:show_frame(frame2), bootstyle=(LIGHT, OUTLINE))
frame1_btn.grid(row=5, column=2, sticky='ew')

main2_btn = ttk.Button(frame2, text="Main Menu", command=lambda:show_frame(frame0), bootstyle=(SECONDARY, OUTLINE))
main2_btn.grid(row=0, column=0, sticky="nw")

frame2_title = ttk.Label(frame2, text="Begin Prompt")
frame2_title.grid(row=1, column=2)

note = ttk.Label(frame2, text="Select a copy style.")
note.grid(row=2, column=2)

copy_list = Listbox(frame2)
copy_list.grid(row=3, column=2, sticky='nsew')

copy_list.insert(0, "About Page")
copy_list.insert(1, "Advertisment")
copy_list.insert(2, "Article")
copy_list.insert(3, "Blog Post")
copy_list.insert(4, "Feature Story")
copy_list.insert(5, "Flyer")
copy_list.insert(6, "Home Page")
copy_list.insert(7, "Landing Page")
copy_list.insert(8, "News Letter")
copy_list.insert(9, "Press Release")
copy_list.insert(10, "Sales Promotion")

frame2_back = ttk.Button(frame2, text="Back", command=lambda:show_frame(frame1), bootstyle=(LIGHT, OUTLINE))
frame2_back.grid(row=4,column=1, sticky='ew')

def fetch_text():
    show_frame(frame3)
    topic = ent.get()
    topic = topic.strip()
    copy_type = copy_list.get(ANCHOR)
    query = "Can you create a " + copy_type + " about " + topic
    text_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a web developer and a copy writer"},
            #company restrictions
            {"role": "assistant", "content": "If the query is not appropriate for a work environment respond with 'Please enter another prompt'"},
            {"role": "assistant", "content": "Do not ask any questions"},
            {"role": "user", "content": query}
        ]
    )
    
    text = text_response.choices[0].message.content
    txt.insert(END, text)

def clear_text():
     txt.delete(1.0,END)

frame2_btn = ttk.Button(frame2, text="Next", command=fetch_text, bootstyle=(LIGHT, OUTLINE))
frame2_btn.grid(row=4, column=3, sticky='ew')

main3_btn = ttk.Button(frame3, text="Main Menu", command=lambda:show_frame(frame0), bootstyle=(SECONDARY, OUTLINE))
main3_btn.grid(row=0, column=0, sticky="nw")

frame3_title = ttk.Label(frame3, text="Text Editor")
frame3_title.grid(row=1, column=2)

text_lbl = ttk.Label(frame3, text="Draft")
text_lbl.grid(row=2, column=2)

txt = Text(frame3)
txt.grid(row=3, column=1, columnspan=3, sticky='nsew')

submit_btn = ttk.Button(frame3, text="Generate new text", command=fetch_text, bootstyle=(LIGHT, OUTLINE))
submit_btn.grid(row=4, column=2)

delete_text = ttk.Button(frame3, text="Clear text", command=clear_text, bootstyle=(LIGHT, OUTLINE))
delete_text.grid(row=5, column=2)

frame3_back = ttk.Button(frame3, text="Back", command=lambda:show_frame(frame2), bootstyle=(LIGHT, OUTLINE))
frame3_back.grid(row=6, column=1, sticky='ew')

frame3_btn = ttk.Button(frame3, text="Next", command=lambda:show_frame(frame4), bootstyle=(LIGHT, OUTLINE))
frame3_btn.grid(row=6, column=3, sticky='ew')

main4_btn = ttk.Button(frame4, text="Main Menu", command=lambda:show_frame(frame0), bootstyle=(SECONDARY, OUTLINE))
main4_btn.grid(row=0, column=0, sticky="nw")

frame4_title = ttk.Label(frame4, text="Create an image for the copy or click next to continue without an image")
frame4_title.grid(row=1, column=1, columnspan=3)

image_lbl = ttk.Label(frame4, text="View Image")
image_lbl.grid(row=2, column=2)

def fetch_image():
    topic = ent.get()
    copy_type = copy_list.get(ANCHOR)
    query = "Create a picture for a " + copy_type + " about " + topic
    image_response = client.images.generate(
        model="dall-e-2",
        prompt=query,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    
    global name
    name = uuid.uuid4()
    png_name = f'{name}.png'
    urllib.request.urlretrieve(image_response.data[0].url, png_name)

    def open_image(*args):
        image_window=Toplevel(window)
        image_window.state('zoomed')
        image_label = ttk.Label(image_window)
        image_label.grid(row=0, column=0, sticky='nsew')
        image = Image.open(png_name)
        image = ImageTk.PhotoImage(image)
        image_label.configure(image=image)
        image_label.image = image

    image_lbl.bind("<Button-1>", open_image)

image_btn = ttk.Button(frame4, text="Generate image", command=fetch_image, bootstyle=(LIGHT, OUTLINE))
image_btn.grid(row=3, column=2)

def clear_html():
    html_area.delete(1.0,END)

def convert_html():
    show_frame(frame5)
    image_src = f'"{name}.png"'
    text_content = txt.get(1.0,END)
    query = "<img src=" + image_src + ">" + "\n" + text_content
    html_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Convert the text provided into HTML format that is styled and colored with CSS"},
            {"role": "user", "content": query}
        ]
    )

    global html
    html = html_response.choices[0].message.content
    html_area.insert(END, html)

frame4_back = ttk.Button(frame4, text="Back", command=lambda:show_frame(frame3), bootstyle=(LIGHT, OUTLINE))
frame4_back.grid(row=4, column=1, sticky='ew')

skip_btn = ttk.Button(frame4, text="Next", command=convert_html, bootstyle=(LIGHT, OUTLINE))
skip_btn.grid(row=4, column=3, sticky="ew")

main5_btn = ttk.Button(frame5, text="Main Menu", command=lambda:show_frame(frame0), bootstyle=(SECONDARY, OUTLINE))
main5_btn.grid(row=0, column=0, sticky="nw")

frame5_title = ttk.Label(frame5, text="Final HTML")
frame5_title.grid(row=1, column=2)

html_area = Text(frame5, height=15, width=120)
html_area.grid(row=2, column=1, columnspan=3, sticky='nsew')

html_btn = ttk.Button(frame5, text="Generate HTML", command=convert_html, bootstyle=(LIGHT, OUTLINE))
html_btn.grid(row=3, column=2)

delete_html = ttk.Button(frame5, text="Clear HTML", command=clear_html, bootstyle=(LIGHT, OUTLINE))
delete_html.grid(row=4, column=2)

def post():
    show_frame(frame6)
    html_name = f'{name}.html'
    file = open(html_name, "w") 
    html = html_area.get(1.0,END)
    file.write(html)
    file.close()
    ent.delete(0,END)
    txt.delete(1.0,END)
    html_area.delete(1.0,END)

frame5_back = ttk.Button(frame5, text="Back", command=lambda:show_frame(frame4), bootstyle=(LIGHT, OUTLINE))
frame5_back.grid(row=5, column=1, sticky='ew')

post_btn = ttk.Button(frame5, text="Finish", command=post, bootstyle=(LIGHT, OUTLINE))
post_btn.grid(row=5, column=3, sticky='ew')

main6_btn = ttk.Button(frame6, text="Main Menu", command=lambda:show_frame(frame0), bootstyle=(SECONDARY, OUTLINE))
main6_btn.grid(row=0, column=0, sticky="nw")

frame6_title = ttk.Label(frame6, text="Success! Your copy was created.")
frame6_title.grid(row=1, column=1)

another_post = ttk.Button(frame6, text="Create another", command=lambda:show_frame(frame1), bootstyle=(LIGHT, OUTLINE))
another_post.grid(row=2, column=1, sticky='ew')

show_frame(frame0)

window.mainloop()