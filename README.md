# 271101_workshop_assignment
# ชยากร ธรรมศิริ
# รหัสนักศึกษา 650610832

# หลักการทำงาน
# โปรแกรม "Index finger of right-hand system" จะมีการตรวจจับนิ้วมือจากมือขวาของเรา โดยมี หลักการในการเขียน Algorithm เบื้องต้น ดังนี้
# 1.สร้าง array ที่มีชื่อว่า  axis เพื่อเก็บข้อมูลตำแหน่งของจุดที่อยู่ระหว่างข้อนิ้วทั้ง 5 ตั้งแต่เลข 0-20 นั่นคือ 21 จำนวน บนแกน 2 แกน
# 2.กำหนดให้ แกน 2 แกนนั้นมีค่า 0 (cx หรือแกน X) และ 1 (cy หรือแกน Y) และสร้าง array โดยเก็บข้อมูลแบบไม่ระบุจำนวน ชื่อว่า finger เพื่อใช้ในการเก็บข้อมูลแบบ string เป็นชื่่อนิ้วที่แสดงตามเงื่อนไขที่สร้างขึ้น
# 3.สร้างเงื่อนไขในการจำแนกนิ้วมือ โดยอิงตามค่าของแนวแกน เช่น ในแนวแกน Y แบบ กลับหัว (หมุน 180 องศา = ตำแหน่งที่ 7 จะมีค่ามากกว่าตำแหน่งที่ 8) ให้มีเงื่อนไขว่า ถ้า ค่า  y ณ ตำแหน่งที่ 8 มีค่าน้อยกว่า ค่า y ณ ตำแหน่งที่ 7 แล้ว ให้เก็บข้อความคำว่า 'Index' นั่นคือนิ้วชี้ ไปไว้ใน array ที่ชื่อว่า finger ซึ่งจะนำไปแสดงผลในภายหลัง พร้อมกับบอกจำนวนตัวแปรที่เกิดขึ้นใน array finger เป็น 1 นั่นคือ มี 1 นิ้วที่สามารถจำแนกได้ เป็นต้น
# 4.ผลลัพธ์ที่ได้และสมบูรณ์ จะเป็นดังภาพ Result1 , Result2 , Result3 และ Result4
# 5.ผลลัพธืที่ไม่สมบูรณ์ จะเป็นดังภาพ Result5 เนื่องจากวางแนวมือเพื่อจำแนกผิด

# CONDITION (เงื่อนไขของโปรแกรม)
# 1.ใช้จำแนกนิ้วมือได้เฉพาะข้างขวาเท่านั้น! ไม่สามารถจำแนกจำนวน และระบุ นิ้วมือข้างซ้ายได้อย่างถูกต้องครบถ้วน
# 2.ไม่สามารถใช้หลังมือในการจำแนกนิ้วมือได้ และต้องวางมือให้เป็นระนาบเรียบ เพื่อไม่ให้ตำแหน่งทั้ง 21 ตำแหน่งคลาดเคลื่อน ดังภาพ Result4 และ Result1
# 3.ไม่สามารถใช้มือทั้ง 2 ข้างจำแนกพร้อมกันได้ เนื่องจากผลลัพธ์ที่ได้จะไม่สมบูรณ์