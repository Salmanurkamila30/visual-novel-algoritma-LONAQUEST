# CHARACTER
define g = Character("{b}Gara{/b}", color="#4682B4")
define l = Character("{b}Lona{/b}", color="#937abf")
define n = Character(None)

# BACKGROUNDS
image bg gara_Komputer = "images/backgrounds/gara_Komputer.png"
image bg cahaya_gara = "images/backgrounds/cahaya_gara.png"
image bg sequencing = "images/backgrounds/sequencing.png"
image bg conditional = "images/backgrounds/conditional.png"
image bg looping = "images/backgrounds/looping.png"
image bg futuristic_2 = "images/backgrounds/futuristic_2.png"
image bg futuristic_3 = "images/backgrounds/futuristic_3.png"
image bg kelas = "images/backgrounds/kelas.png"
image bg komputer2_gara = "images/backgrounds/komputer2_gara.png"


# ICON LEVEL MENU
image icon_level1 = "images/option/level1.png"
image icon_level2 = "images/option/level2.png"
image icon_level3 = "images/option/level3.png"
image icon_reset  = "images/option/reset.png"
image kunci = "images/option/kunci.png"


# VARIABLES 
default score_total = 0       
default score1 = 0           
default score2 = 0            
default score3 = 0            
default count_hi = 0
default tooltip = ""

# INITIATION 
init python:
    config.always_shown_screens = [ 'hud_reset' ] 

# SCREEN LEVEL MENU
screen level_menu():
    tag menu
    add "images/backgrounds/kelas.png"
    on "show" action Hide("window") 

    # Judul
    vbox:
        xalign 0.5
        yalign 0.12
        spacing 16
        text "{b}Pilih Level{/b}" size 80 color "#ffffff" xalign 0.5

    # Skor
    frame:
        xalign 0.5
        yalign 0.22
        background None
        vbox:
            spacing 4
            text "Skor Rata-rata: " size 30 color "#ffffff" xalign 0.5
            text "Level 1= [score1]      Level 2= [score2]       Level 3= [score3]" size 30 color "#ffffff" xalign 0.5

    # Tombol Level
    hbox:
        xalign 0.5
        yalign 0.7
        spacing 5

        # Level 1
        imagebutton:
            idle "images/option/level1.png"
            hover "images/option/level1.png"
            action Return("scene1")
            hovered SetVariable("tooltip", "{b}Sequencing & Abstraksi{/b}")

        # Level 2
        if score1 >= 50:
            imagebutton:
                idle "images/option/level2.png"
                hover "images/option/level2.png"
                action Return("scene2")
                hovered SetVariable("tooltip", "{b}Conditional & Dekomposisi{/b}")
        else:
            imagebutton:
                idle "images/option/kunci.png"
                hover "images/option/kunci.png"
                action NullAction()
                hovered SetVariable("tooltip", "{b}Level masih terkunci, Raih ≥ 50 pada Level 1{/b}")

        # Level 3
        if score2 >= 40:
            imagebutton:
                idle "images/option/level3.png"
                hover "images/option/level3.png"
                action Return("scene3")
                hovered SetVariable("tooltip", "Looping")
        else:
            imagebutton:
                idle "images/option/kunci.png"
                hover "images/option/kunci.png"
                action NullAction()
                hovered SetVariable("tooltip", "{b}Level masih terkunci, Raih ≥ 50 pada Level 2{/b}")
    if tooltip:
        frame:
            xalign 0.5
            yalign 0.92
            background None
            text tooltip color "#ffffff" size 32 xalign 0.5
    hbox:
            xpos 0.90   
            ypos 0.02 
            anchor (1, 0) 
            spacing 10 
            
            #home
            imagebutton:
                idle "images/option/home.png" 
                hover "images/option/home.png"
                action Jump("menu_level") 
                hovered SetVariable("tooltip", "Kembali ke Menu Level")

            #reset
            imagebutton:
                idle "images/option/reset.png"
                hover "images/option/reset.png"
                action Jump("reset_game") 
                hovered SetVariable("tooltip", "Reset semua progress")


# SCREEN HUD
screen hud_reset():
    
   
    hbox:
        xpos 0.90   
        ypos 0.02 
        anchor (1, 0)
        spacing 10 
        
        #home
        imagebutton:
            idle "images/option/home.png"
            hover "images/option/home.png"
            action Jump("menu_level") 
            hovered SetVariable("tooltip", "Kembali ke Menu Level")

        #reset
        imagebutton:
            idle "images/option/reset.png"
            hover "images/option/reset.png"
            action Jump("reset_game")
            hovered SetVariable("tooltip", "Reset semua progress")

# Opening movie image 
image opening_1 = Movie(play="images/video/video_1.webm", side_mask=True, size=(1920,1080))
image opening_2 = Movie(play="images/video/video_2.webm", side_mask=True, size=(1920,1080))


# START
label start:

    scene bg gara_Komputer
    play music "audio/ketik.mp3" fadein 0.8

    n "Di kelas Informatika, Gara menatap layar komputer, dahinya berkerut penuh kebingungan."
    g "Sequencing, conditional, looping… konsepnya rumit banget. Kira-Kira gimana ya cara kerjanya di dunia nyata?"

    window hide
    show expression Movie(size=(1920, 1080), play="images/video/video_1.webm", loop=True) as bg_vid
    pause 5.0
    
    scene bg futuristic_2 with fade 

    stop music fadeout 0.5
    show gara at left
    play sound "audio/kaget.mp3"
    play music "audio/tenang.mp3" fadein 1.0
    show garat at left
    g "W-Woi! Apa yang terjadi! Kenapa aku di sini!?"
    stop sound
    show lona at right
    show lonab at right
    l "Tidak perlu panik, Gara. Selamat datang di {b}Dimensi Logika{/b}."
    hide lonab
    hide garat
    show lonab at right
    l "Aku Lona, AI penjaga konsistensi logika di dimensi ini."
    hide lonab

    show garab at left
    g "Jadi... aku masuk ke sini karena bingung dengan pelajaran Informatika?"
    hide garab

    show lonab at right
    l "Benar. Untuk kembali, kamu harus menguasai {b}Tiga Kunci Logika{/b} yang kamu pelajari: Sequencing, Conditional, dan Looping."
    hide lonab

    show lonab at right
    l "Bersiaplah. Kita mulai dari Kunci pertama."
    hide lonab
    hide gara
    hide lona
    stop music fadeout 0.5
    hide window
    jump menu_level

# MENU LEVEL 
label menu_level:
    $ tooltip = ""
    play music "audio/materi.mp3" fadein 1.0
    $ pilih = renpy.call_screen("level_menu")
    
    if pilih == "scene1":
        jump scene1
    elif pilih == "scene2":
        jump scene2
    elif pilih == "scene3":
        jump scene3
    elif pilih == "reset":
        jump reset_game
    else:
        jump menu_level


# RESET
label reset_game:
    $ score_total = 0
    $ score1 = 0
    $ score2 = 0
    $ score3 = 0
    $ count_hi = 0
    
    n "Progress kamu sudah di-reset."
    
    jump menu_level


# MODULE 1 – SEQUENCING & ABSTRAKSI 
label scene1:

    $ level_temp = 0
    $ level1_max = 100.0   

    scene bg sequencing with fade
    play music "audio/games2.mp3" loop fadein 0.8 volume 0.5

    show lona 
    show lonab 
    l "Selamat datang di Level 1: {b}Sequencing {/b} dan {b}Abstraksi{/b}."
    l "Kita mulai dengan {b}Abstraksi{/b}! Konsep ini intinya adalah {b}menyaring dan fokus pada detail yang penting saja{/b}. "
    l "Setelah itu, kita akan menyusun langkah-langkah secara {b}berurutan dan logis{/b}, yaitu {b}Sequencing{/b}. Ibarat membuat resep masakan, urutan langkahnya tidak boleh salah."
    l "Nah, sekarang kita lanjut ke soal ya. "
    hide lonab
    

    jump soal_abstraksi

label soal_abstraksi:

    show lonab 
    l "Bayangkan kamu membuat aplikasi pemesanan makanan."
    hide lonab
    show lonab 
    l "Informasi apa yang wajib muncul di halaman utama?"
    hide lonab
    show lona at right

    menu:
        "A. Riwayat chat panjang pelanggan":
            jump salah_abstraksi
        "B. Menu, harga, dan tombol pesan":
            jump benar_abstraksi
        "C. Cerita sejarah restoran":
            jump salah_abstraksi
        "D. Foto dapur belakang":
            jump salah_abstraksi
label salah_abstraksi:
    hide lona
    stop sound
    show lonah
    play sound "audio/wrong.mp3"  noloop 
    l "Itu {b}kurang relevan{/b} untuk tujuan utama halaman."
    l "Abstraksi adalah tentang {b}menyaring detail yang tidak perlu.{/b} Pengguna di halaman utama hanya perlu tahu: menu apa yang tersedia dan bagaimana cara memesan."
    l "Fokuslah pada {b}fungsi inti aplikasi!{/b} Ayo lanjutkan ke tantangan berikutnya, Gara."
    stop sound
    hide lonah
    jump soal_sequencing

label benar_abstraksi:
    $ level_temp += 50  
    hide lona
    play sound "audio/benar.mp3"  noloop 
    show lonas
    l "Tepat! Bagus sekali kamu sudah menangkap inti abstraksi."
    stop sound
    l "Pertahankan perhatian seperti itu, lanjutkan!"
    hide lonas
    jump soal_sequencing


# SEQUENCING – MEMBUAT TEH
label soal_sequencing:

    show lonab
    l "Pilih langkah pertama membuat teh panas."
    hide lonab

    show lona at right
    menu:
        "Masukkan gula":
            jump salah_sequencing
        "Rebus air":
            jump langkah2
        "Tuang air panas":
            jump salah_sequencing
        "Sajikan":
            jump salah_sequencing
        "Masukkan teh":
            jump salah_sequencing
label langkah2:
   
    hide lona
    play sound "audio/benar.mp3"  noloop 
    show lonas
    l "Mantap!! Langkah yang Tepat. Lanjutkan langkah Ke-2!"
    hide lonas
    stop sound
    show lona at right
    menu:
        "Masukkan gula":
            jump salah_sequencing
        "Rebus air":
            jump salah_sequencing
        "Tuang air panas":
            jump salah_sequencing
        "Sajikan":
            jump salah_sequencing
        "Masukkan teh":
            jump langkah3
    hide lona
label langkah3:
    
    hide lona
    play sound "audio/benar.mp3"  noloop 
    show lonas
    l "Bagus, lanjutkan langkah Ke-3. Kamu sudah di jalur yang benar."
    hide lonas
    stop sound
    show lona at right
    menu:
        "Masukkan gula":
            jump langkah4
        "Rebus air":
            jump salah_sequencing
        "Tuang air panas":
            jump salah_sequencing
        "Sajikan":
            jump salah_sequencing
        "Masukkan teh":
            jump salah_sequencing
    hide lona
label langkah4:
    hide lona
    
    play sound "audio/benar.mp3"  noloop 
    show lonas
    l "Good Job, konsistensi bagus tetap fokus dan lanjut langkah Ke-4!"
    hide lonas
    stop sound

    show lona at right
    menu:
        "Masukkan gula":
            jump salah_sequencing
        "Rebus air":
            jump salah_sequencing
        "Tuang air panas":
            jump langkah5
        "Sajikan":
            jump salah_sequencing
        "Masukkan teh":
            jump salah_sequencing
    hide lona
label langkah5:
    hide lona
    play sound "audio/benar.mp3"  noloop 
    show lonas
    l "Bagus! Langkah terakhir, hampir selesai!"
    hide lonas
    stop sound
    show lona at right
    menu:
        "Masukkan gula":
            jump salah_sequencing
        "Rebus air":
            jump salah_sequencing
        "Tuang air panas":
            jump salah_sequencing
        "Sajikan":
            jump benar_sequencing
        "Masukkan teh":
            jump salah_sequencing
    hide lona
label salah_sequencing:
    hide lona
    play sound "audio/wrong.mp3"  noloop 
    show lonah
    l "Urutannya {b}salah!{/b} Sequencing menuntut langkah yang {b}logis dan berurutan.{/b} Kamu tidak bisa menuang air panas jika airnya belum direbus!"
    stop sound

    l "Setiap langkah bergantung pada yang sebelumnya. Coba pikirkan kembali alur kerjamu di dapur."
    l "Coba sekali lagi, pikirkan langkah-langkah membuat teh. {b}Kamu pasti bisa memperbaikinya, Semangat!{/b}"
    hide lonah
    stop music fadeout 0.5
    jump soal_sequencing

label benar_sequencing:
    $ level_temp += 50
    hide lona
    play sound "audio/benar.mp3"  noloop 
    show lonas
    l "Kamu sudah menguasai {b}sequencing!{/b}"
    stop sound
    l "Hebat, kamu paham alur proses dengan baik."
    hide lonas

    $ score1 = int(round((level_temp / level1_max) * 100.0))
    show lona
    l "Level 1 selesai! {b}Skor Level 1: [score1].{/b}"
    hide lona
    hide lona
    stop music fadeout 0.5
    jump menu_level

# MODULE 2 – CONDITIONAL
label scene2:

    $ level_temp = 0
    $ level2_max = 100.0  

    scene bg conditional with fade
    play music "audio/games2.mp3" loop fadein 0.8 volume 0.5

    show lonab 
    l "Selamat datang di Level 2: {b}Conditional{/b} (Percabangan) dan {b}Dekomposisi{/b}."
    l "Kita mulai dengan {b}Dekomposisi{/b}. Ini adalah kemampuan untuk {b}memecah masalah besar menjadi tugas-tugas kecil{/b} yang mudah diselesaikan satu per satu. "
    l "Kemudian, kita akan belajar {b}Percabangan{/b}. Ini adalah cara program {b}mengambil keputusan{/b} ('JIKA' suatu kondisi benar, lakukan Aksi X, 'JIKA TIDAK', lakukan Aksi Y)."
    l "Ingat ya, Percabangan (Conditional) berfokus pada {b}membuat SATU PILIHAN LOGIS{/b}. Berbeda dengan Looping di Level 3 yang akan {b}mengulang aksi BERKALI-KALI{/b}."
    l "Nah, sekarang kita lanjut ke soal ya. "
    hide lonab

    show lonab
    l "Apa langkah paling tepat merapikan inventaris?"
    hide lonab
    show lona at right
    menu:
        "A. Membeli rak baru":
            jump salah_dekom
        "B. Mengelompokkan barang → pisahkan stok habis → catat ulang":
            jump benar_dekom
        "C. Membiarkan saja":
            jump salah_dekom
        "D. Membakar gudangnya":
            jump salah_dekom
   
label salah_dekom:
    hide lona
    play sound "audio/wrong.mp3" fadein 1.0 noloop 
    show lonah
    l "Dekomposisi harus {b}terarah{/b} dan dapat dikelola. Membeli rak baru adalah solusi fisik, bukan langkah logis untuk memecah masalah."
    stop sound
    l "Dekomposisi memecah tugas besar {b}'merapikan'{/b} menjadi langkah-langkah kecil yang logis {b}'mengelompokkan', 'memisahkan', 'mencatat'{/b}."
    l "Pikirkan langkah-langkah kecil yang bisa kamu lakukan sekarang. Lanjut ke tantangan Conditional!"
    hide lonah
    jump percabangan

label benar_dekom:
    $ level_temp += 50
    hide lona
    play sound "audio/benar.mp3"  noloop 
    show lonas
    l "Bagus! Itu contoh dekomposisi yang tepat."
    stop sound
    l "Pilihan tepat! kamu paham cara memecah masalah menjadi langkah."
    hide lonas
    jump percabangan

label percabangan:

    show lonab
    l "Soal selanjutnya adalah {b}percabangan (Conditional).{/b}"
    l "Intinya adalah membuat komputer {b}mengambil keputusan{/b} berdasarkan kondisi yang ada. Contohnya: {b}IF (Kondisi Benar), lakukan Aksi X. ELSE, lakukan Aksi Y.{/b}"
    l "Coba terapkan: IF hujan == TRUE, apa keputusan logis yang akan diambil?"
    hide lonab
    show lona at right
    menu:
        "Keluar tanpa melihat cuaca":
            jump salah_conditional
        "Mengecek hujan dan membawa payung":
            jump benar_conditional
        "Tidak jadi keluar":
            jump salah_conditional
label salah_conditional:
    hide lona
    play sound "audio/wrong.mp3" fadein 1.0 noloop 
    show lonah
    l "Kesalahan fatal! Kamu tidak mempertimbangkan {b}Kondisi (IF){/b} sebelum bertindak."
    l "Komputer harus selalu {b}memeriksa kondisi{/b} (IF = Hujan) sebelum mengambil tindakan yang sesuai (THEN = Bawa Payung). Kamu harus selalu berpikir responsif."
    l "Kamu harus lebih teliti. Coba berpikir seperti komputer: {b}Cek kondisi sebelum bertindak.{/b}"
    stop sound
    hide lonah
    
    $ score2 = int(round((level_temp / level2_max) * 100.0))
    show lonab
    l "Level 2 selesai! Skor Level 2: [score2]."
    hide lonab
    if score2 < 50:
        show lonab
        l "Nilai Level 2 kurang dari 50. Level 3 belum terbuka. "
        hide lonab
    else:
        show lonab
        l "Selamat kamu membuka jalan menuju Level 3!"
        hide lonab

    jump menu_level

label benar_conditional:
    $ level_temp += 50
    hide lona
    play sound "audio/benar.mp3"  noloop 
    show lonas
    l "Good job! Kamu mempertimbangkan kondisi sebelum bertindak."
    stop sound
    l "Keputusan logis! Pertahankan pemikiran seperti itu."
    hide lonas

    $ score2 = int(round((level_temp / level2_max) * 100.0))
    show lonab
    l "Level 2 selesai! Skor Level 2: [score2]."
    hide lonab
    if score2 < 50:
        show lonab
        l "Nilai Level 2 kurang dari 50. Level 3 belum terbuka. "
        hide lonab
    else:
        show lonab
        l "Selamat kamu membuka jalan menuju Level 3!"
        hide lonab

    jump menu_level


# MODULE 3 – LOOPING
label scene3:

    $ level_temp = 0
    $ level3_max = 100.0 
    scene bg looping with fade
    show lona 

    play music "audio/games2.mp3" loop fadein 0.8 volume 0.5
    show lonab 
    l "Selamat datang di Level 3: {b}Looping{/b} (Pengulangan)."
    l "Setelah kita belajar {b}memilih jalur (Conditional){/b}, sekarang kita belajar {b}mengulang jalur secara cerdas{/b}."
    l "{b}Looping{/b} adalah tentang {b}pengulangan proses secara efisien{/b} untuk menghemat kode, waktu, dan sumber daya."
    l "Prinsipnya: {b}Lakukan tugas yang sama berulang kali, tapi dengan cara terpintar.{/b}"
    l "Kita lanjut ke soalnya, Yuk."
    hide lonab
    show lona at right
    menu:
        "Rute A: Pendek tapi banyak hambatan":
            jump salah_rute
        "Rute B: Sedang, aman, stabil":
            $ level_temp += 50  
            jump benar_rute
        "Rute C: Panjang tapi lurus sekali":
            jump salah_rute
    hide lona
label salah_rute:
    hide lona
    play sound "audio/wrong.mp3" fadein 1.0 noloop 
    show lonah
    l "Rute yang kamu pilih kurang efisien. Dalam pemrograman, Looping harus mencari {b}jalur yang paling optimal untuk diulang{/b}. Ingat, pengulangan harus hemat. Coba lagi!"
    stop sound 
    hide lonah
    jump looping_hi 

label benar_rute:
    hide lona
    play sound "audio/benar.mp3"  noloop 
    show lonas
    l "Tepat! Pilihan yang matang kamu telah memahami trade-off."
    stop sound
    hide lonas

    show lonab
    l "Sekarang latihan while-loop."
    hide lonab

    $ count_hi = 0
    jump looping_hi

label looping_hi:

    show lona at right
    menu:
        "Hi":
            $ count_hi += 1
            $ level_temp += 10  
            jump check_hi
        "Hallo":
            jump salah_hi
    hide lona
label check_hi:

    if count_hi == 5:
        jump correct_hi
    else:
        play sound "audio/benar.mp3" fadein 1.0 noloop 
        hide lona
        show lonas
        l "Jumlah {b}'Hi'{/b} sekarang {b}[count_hi].{/b} Lanjutkan."
        hide lonas
        stop sound
    jump looping_hi

label correct_hi:
    hide lona
    show lonas
    play sound "audio/benar.mp3" fadein 1.0 noloop 
    l "Bagus! Kamu memilih {b}'Hi'{/b} 5 kali."
    l "Kamu sangat konsisten! Itu inti dari loop yang efektif."
    stop sound
    hide lonas

    $ score3 = int(round((level_temp / level3_max) * 100.0))
    show lona
    l "Level 3 selesai! {b}Skor Level 3: [score3].{/b}"
    stop music fadeout 0.5
    show lona
    jump ending
label salah_hi:
    hide lona
    play sound "audio/wrong.mp3" fadein 1.0 noloop 
    show lonah
    l "Perintah yang diulang harus {b}konsisten{/b}. Jika loopnya adalah 'Hi', kamu tidak bisa memasukkan 'Hallo'. Pikirkan apa yang seharusnya diulang."

    hide lonah
    jump looping_hi 
    stop sound
    stop music fadeout 0.5
    jump ending

# ENDING 
label ending:
    play music "audio/tenang.mp3" fadein 1.0 
    hide lona
    python:
        try:
            score_total = int(round((score1 + score2 + score3) / 3.0))
        except Exception:
            score_total = 0
    show lonab
    l "Nilai akhir Gara adalah {b}[score_total] poin.{/b}"
    hide lonab
    if score_total >= 50:
        show lonas
        l "Kamu luar biasa!"
        hide lonas
    elif score_total >= 30:
        show lonas
        l "Kemampuanmu bagus!"
        hide lonas
    else:
        show lonab
        l "Tenang, kamu bisa mengulang modulnya."
        hide lonab

    scene bg futuristic_3 with fade

    show lona at right
    show gara at left

    show lonab at right
    l "Selamat Gara! Kamu telah {b}mengaktifkan{/b} Tiga Kunci Logika."
    hide lonab

    show lonab at right
    l "Algoritma bukan hafalan, tapi {b}cara berpikir.{/b}"
    hide lonab
    
    hide gara
    
    window hide
    show expression Movie(size=(1920, 1080), play="images/video/video_2.webm", loop=True) as bg_vid
    pause 3.0
    scene bg komputer2_gara with dissolve
    g "Pak… sekarang saya ngerti. Algoritma itu {b}soal menyusun logika.{/b}"

    n "Petualangan di Dimensi Logika berakhir."

    stop music fadeout 0.5

    return
