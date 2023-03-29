# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/blck.png"

# Deklarasikan karakter yang digunakan di game.
define te = Character('Theo', color="#c8ffc8")

#rena----------------------------------------------------
define re = Character('Rena', color="#ebc8ff")
image rena smp ="images/char/rena_smp.png"
image rena smp maaf = "image/char/rena_smp_maaf.png"
#tirta------------------------------------------------------------
define ti = Character('Tirta', color="#0072ec")
image tirta ="images/char/tirta/tirta_normal.png"
image tirta merem = "images/char/tirta/tirta_merem.png"
image tirta nyengir = "images/char/tirta/tirta_nyengir.png"
image tirta panik = "images/char/tirta/tirta_panik.png"
#guru-------------------------------------------------------------------
define gu = Character('guru', color="#ecb500" )
image guru = "images/char/guru/guru_biasa.png"
image guru merem = "images/char/guru/guru_merem.png"

#unknow ???----------------------------
define un1 = Character('???',color = "#ebc8ff")

#untuk splashscreen
label splashscreen:
    scene black
    with Pause(1)

    show text "game ini hanya untuk bersenang senang" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "cerita yang terkandung di dalamnya berupa cerita fiktif \ndan jika ada nama, latar yang sama, itu merupakan kebetulan dan hal tidak disengaja" with dissolve
    with Pause(4)

    hide text with dissolve
    with Pause(1)

    scene splashscreen with dissolve
    with Pause(2)

    show black with dissolve
    with Pause(1)
    return

# Game dimulai disini.
label start:

    scene bg blck with dissolve
    stop sound 
    play music "audio/SAD.mp3"
   
    te "aku akan melakukannya. Aku akan menyatakan cinta sore ini"
    te "aku akan menembak rena. gadis yang aku sukai."

    "sudah jam 4 nih, aku langsung eksekusi saja"
    scene lorong with dissolve
    show rena smp with dissolve
    te "rena...."

    menu :
        "gimana aku nembaknya"
        "langsung gas tembak":
            te "mmm... maukah kamu mendampingiku sebagai pacar?"
        "gombal dulu":
            te "senja ini sepertinya terlihat lebih enak dipandang, jadi aku ingin mengatakan sesuatu..."
            te "rena, apakah kamu mau selalu bersamaku..."
            te "dari pacaran hingga kita bisa menikah?"

    re "..."

    re "maaf aku tidak bisa, kamu chunibyou, aku belum bisa menerimamu."
    te "Kamu yakin?"
    show rena_smp_maaf 
    re "aku yakin, maaf ya..."


    scene bg blck with dissolve
    with Pause(1)
    "Dengan begitu aku, berintrospeksi diri dan mulai berubah agar kegalauannya tidak berubah."
    "Hingga 5 tahun kemudian, aku sudah menginjak kelas 3 sma di SMA Mekarsari. aku mulai melupakannya dengan kejadian tersebut"
    stop music 


    scene  chap1 with dissolve
    with Pause(3)
    play music "audio/kantin.mp3"
    scene  kantin with dissolve
    
    

    "Waktu menunjukkan jam 12 siang, sudah waktunya istirahat."
    "aku bersama temanku Tirta pergi ke kantin bersama karena memang sudah menjadi kebiasaan kami untuk makan bareng di kantin"
    "namun di hari ini ..."

    show tirta with dissolve
    ti "Theo, aku penasaran"
    ti "belakangan ini kok kamu keliatan lebih cerah...?"
    ti "padahalkan sebelumnya kamu keliatan kusam?"
    te "owh aku baru move on"
    te "ingat yang aku pernah ceritakan beberapa saat yang lalu"
    ti " oh... kisah 5 tahun yang lalu?"
    te "benar, aku sudah tidak terlalu mikirin lagi tentang dia"
    ti "oh pantesan wajahmu lebih berseri daripada sebelumnya"
    ti "bagus lah..."
    ti "jadi kamu bisa tambah mood biar bisa belajar"
    ti "supaya bisa mengerjakan ujian SBMPTN"
    te "bener juga sih"
    te "oh ya, kamu belum pesen makan kan?, pesen dulu gih..."
    ti "iya iya..."
    hide tirta with dissolve
    with Pause(2)
    
   
    "setelah itu, Tirta pergi ke meja pemesanan untuk membeli makanan"
    "Setelah beberapa saat menunggu Tirta kembali dengan membawa makanan, sedangkan saya sendiri bawa sudah bawa makan dari rumah"
    show tirta with dissolve
    ti "maaf lama..."
    "Tirta langsung meletakkan soto pesanannya di meja dan menuangkan sambal"
    ti "oh ya, aku dapat intel nih... , anjay intel"
    ti "aku dapat informasi kalau ada anak pindahan di kelas 2, dan dia cewek cantik loh..."
    te "memang seberapa cantik?"
    ti "cantik beut sampe banyak cewek seangkatannya mengimri..."
    ti "malahan banyak cowok seangkatannya bahkan angkatan kita ngincar dia"
    te "he.... sejak kapan dia di sini"
    ti "entahlah, informasiku kurang"
    te "ya... gak asyik lu"
    show tirta nyengir with dissolve
    ti "kenapa, mau ngincer juga?" 
    ti "padahal baru saja move on, masak iya mau galau lagi?"
    te "gak juga..."
    te "Cuma penasaran saja, kok bisa sampe cowok seangkatan kita pada naksir"
    te "buruan makan gih, kuah sotomu nyerap lo nanti..."
    show tirta with dissolve
    ti "oh ya juga"
    ti "saking asiknya kan... sampe kelupaan kalo udah ambil makan"
    ti "yaudah makan dulu"
    te "ok"

    "mereka pun lanjutkan makannya hingga selesai. "
    scene black with dissolve
    with Pause(1)
    
    scene classroom with dissolve


    "setelah istirahat makan, kami kembali ke kelas"
    "karena masih ada waktu sebelum masuk jam pelajaran, kami mengobrol lagi sembari menunggu jam pelajaran dimulai"

    show tirta with dissolve
    te "tirta... mengenai cewek tadi..."
    show tirta nyengir with dissolve
    ti "ciee... penasaran ya"

    menu:
        "cie penasaran ya?"
        "balas jawab":
            te "kalo iya kenapa"
            ti "hehe jangan jangan kamu naksir ya...."
            te "menurutmu?..."
            show tirta merem with dissolve
            ti "hmm... menurutku..."
            show tirta with dissolve
            ti "kayaknya gak deh, mengingat kamu ini wibu..."
            ti "pasti kamu lebih prioritaskan waifu 2D"
            te "buset..."
            te "mentang-mentang dipanggil wibu tapi gak begitu juga sih"
            te "ya meskipun beberapa orang kayak begitu, tapi aku TIDAK TERMASUK!! "
            te "tapi ya...  yang bilang aku setuju sih bagian jawaban dari pertanyaanmu tadi"
        "ngeles":
            te "eee....."
            te "oh ya nanti kan matematika kan?"
            show tirta merem with dissolve
            ti "loh kok ngeles..."
            show tirta nyengir with dissolve
            ti "apa jangan jangan bener, kamu penasaran?"
            te "pr kamu sudah dikerjakan belum?"
            te "soalnya nanti dikumpulin lo..."
            show tirta panik with dissolve
            ti "LAH!!!..."
            ti "iya juga, aduh...."
            ti "mana tinggal 15 menit lagi"
            show tirta merem with dissolve
            ti "Theo, bisa gak aku liatin tugasmu?"
            te "heee... kamu mau liatin pr ku?"
            te "boleh sih, cuma jangan jailin aku kayak gini lagi"
            show tirta with dissolve
            ti "ya deh... ya deh"
            te "yaudah "
            "akhirnya Tirta mengerjakan prnya sebelum jam pelajaran berikutnya dimulai dan aku berhasil ngeles"

    hide tirta with dissolve
    with Pause(1)
            
    "jam pelajaran dimulai dan pelajarannya adalah matematika."
    "jujur ini agak merepotkan mengingat jamnya di siang hari, pasti banyak yang ngantuk"
    "apalagi kalau jam pelajarannya matematika"
    "tapi aku harus bisa memahami pelajaran ini karena dalam waktu beberapa bulan aku mesti melaksanakan SBMPTN"
    "mumpung lagi mood"

    with Pause(2)

    "ah dah masuk ternyata,"
    show guru with dissolve
    gu "baik anak anak sekarang waktunya kuis matematika"
    gu "kalian bisa gunakan kertas coretan untuk bisa menjawabnya…"
    gu "materinya tentang propabilitas"
    gu "dengarkan baik baik ya…"
    gu "ada berapa cara Menyusun kata \"SEKOLAH\" "

    menu: 
        "ada berapa cara Menyusun kata \"matematika\" "
        "\nanda boleh gunakan catetan buat mengerjakannya"
        "menjawab jawaban":
                            te "saya pak"
                            gu "berapa?"
 
                            menu: 
                                "ada berapa cara Menyusun kata \"matematika\" "
                                "\nanda boleh gunakan catetan buat mengerjakannya"
                                "151200":
                                        te "151200"
                                        gu "benar sekali, selamat ada mendapatkan hadiah"
                                        te "beneran pak?..."
                                        te "apa itu?"
                                        gu "kepuasan hati karena menjawabnya dengan benar"
                                        te "ya ampun pak, bisa aja bercandanya"
                                        show guru merem with dissolve
                                        gu "anggep aja ice breaking, soalnya saya tau jam segini pasti mengantuk"
                                        show guru with dissolve
                                        gu "tenang aja, saya masukan anda di nilai keaktifan"

                                "151100":
                                        te "151100"
                                        show guru merem with dissolve
                                        gu "selamat anda  bisa mencoba menghitung lagi karena hasilnya belum bener"
                                        te "lah.. pak…"
                                        te "kok begitu bercandanya"
                                        show guru with dissolve
                                        gu "soalnya jam segini bagus kalo pake ice breaking"

                                "362820":
                                        te "362820"
                                        show guru merem with dissolve
                                        gu "kau yakin dengan jawabannya?"
                                        te "yakin pak"
                                        show guru with dissolve
                                        gu "nampaknya kamu belum hoki soalnya jawaban anda salah"
                                        te "lah.. pak…"
                                        te "kok begitu bercandanya"
                                        gu "saya tau jam segini pasti banyak yang ngantuk"
                                        gu "makanya saya kasih candaan"


                                "603800":
                                        te "603800"
                                        show guru merem with dissolve
                                        gu "hmmm kurang tepat"
                                        te "aduh kurang tepat ternyata"
                                        show guru with dissolve
                                        gu "mungkin bisa menjawab benar lain kali"
                                "10000":
                                        te "10000"
                                        gu "ceban ya…"
                                        gu "maaf jawaban kurang tepat"
                                        gu "mungkin bisa menjawab jawaban benar lain kali"

        "gak jawab dulu":
                            te " saya tidak dulu pak"
                            gu "yakin, lumayan loh dapet nilai keaktifan. Bisa masuk di nilai rapor"
                            te "belum selesai hitung pak"
                            gu "ya sudah, mungkin yang lainnya..."

    
    hide guru with dissolve
    scene bg blck with dissolve

    "setelah beberapa kuis dan candaan dari pak guru, akhirnya kelas berakhir pukul 3 sore"
    "karena aku tidak ada kegiatan, aku langsung pulang ke rumah"

    te "kelas tadi agak"
    te " hari ini habis kelas, panas, haus lagi..."
    te "minum dulu ah..."
    te "mumpung ada mesin nih..."

    te "apa ya..."
    "..."
    un1  "theo... ini beneran theo ya"
    te "i... iya..."
    "rasanya kok gak asing sama suaranya, rasanya seperti... 6 tahun lalu"
    un1 "akhirnya..."
    scene closeup with dissolve
    with Pause(2)
    scene closeup_nangis with dissolve
    un1 "lama gak ketemu ya"
    un1 "ini aku..."
    re "rena..."
    scene black
    te "he..."

    
    
    "terima kasih untuk mecoba game ini, tunggu full gamenya ya...\nbuild with ❤️ fajrul"
    scene black with dissolve
    with Pause(1)
    return
