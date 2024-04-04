import pywhatkit as pw

txt = """hello world this is dinesh from pokhara. i live in new Baneswor kathmandu can we collaborat4e on the git hub thank you!!!"""
pw.text_to_handwriting(txt, "hy.png", [0, 0, 138])
print("end")
