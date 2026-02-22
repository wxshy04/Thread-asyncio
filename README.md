1. Multi-threading Analysis
ไฟล์: thread_demo.py

แนวคิดการทำงาน:
จำลองสถานการณ์การดาวน์โหลดไฟล์หลายไฟล์พร้อมกัน (File Downloading Simulation) โดยใช้ Thread เพื่อให้ CPU สามารถสลับไปทำงานอื่นได้ในขณะที่รอการตอบสนองจาก I/O

เหมาะสำหรับ:

งานที่ต้องรอ Hardware (I/O Bound)

การโหลดไฟล์ หรือการอ่านข้อมูลจาก Disk

การสื่อสารผ่านระบบเครือข่ายเบื้องต้น

2. Asyncio Deep Dive
ไฟล์: asyncio_demo.py

แนวคิดการทำงาน:
การดึงข้อมูลจากเว็บไซต์หลายแหล่งพร้อมกัน (Web Scraping/API Simulation) โดยใช้ระบบ Event Loop ซึ่งเน้นการทำงานแบบ Non-blocking ผ่านคำสั่ง:

async / await

asyncio.gather()

ข้อดี: โปรแกรมไม่เกิดการ Block ในขณะรอข้อมูลจาก Network ทำให้จัดการหลายงานได้ใน Thread เดียว

3. Process Pool Calculation
ไฟล์: processpool_demo.py

แนวคิดการทำงาน:
การคำนวณค่าทางคณิตศาสตร์ระดับสูง (เช่น Factorial) โดยการกระจายงานไปยัง Multiple CPU Cores เพื่อใช้ทรัพยากรเครื่องอย่างเต็มประสิทธิภาพ

เหมาะสำหรับงานคำนวณหนัก (CPU-Bound):

งานด้าน AI / Machine Learning

การประมวลผลข้อมูลขนาดใหญ่ (Data Processing)

การคำนวณสูตรทางคณิตศาสตร์ที่มีความซับซ้อน
