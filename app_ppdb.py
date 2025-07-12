import streamlit as st

# Pengetahuan terkait PPDB Sekolah
ppdb_knowledge = [
    "PPDB adalah singkatan dari Penerimaan Peserta Didik Baru.",
    "PPDB biasanya dilakukan secara online di banyak daerah.",
    "Syarat utama mendaftar PPDB adalah memiliki ijazah sekolah sebelumnya.",
    "Dokumen yang sering dibutuhkan: KK, Akta Kelahiran, dan KTP orang tua.",
    "Jalur PPDB meliputi zonasi, afirmasi, prestasi, dan perpindahan tugas orang tua.",
    "Jalur zonasi mengutamakan jarak tempat tinggal ke sekolah.",
    "Jalur afirmasi untuk siswa dari keluarga kurang mampu.",
    "Jalur prestasi berdasarkan nilai rapor atau kejuaraan.",
    "Jalur perpindahan tugas untuk anak ASN yang pindah tugas.",
    "Pendaftaran PPDB biasanya dibuka pertengahan tahun ajaran.",
    "Setiap sekolah memiliki kuota masing-masing untuk tiap jalur.",
    "Pengumuman hasil seleksi PPDB dilakukan secara online.",
    "Jika diterima, siswa wajib melakukan daftar ulang.",
    "Daftar ulang biasanya dilakukan di sekolah tujuan.",
    "Jika tidak daftar ulang, hak diterima bisa gugur.",
    "Beberapa sekolah favorit memiliki persaingan ketat.",
    "PPDB transparan dan dapat dipantau secara daring.",
    "Orang tua dapat mengajukan sanggahan jika ada kesalahan data.",
    "Siswa dapat memilih lebih dari satu sekolah tujuan.",
    "Setiap daerah memiliki aturan PPDB yang berbeda.",
    "PPDB mengutamakan prinsip keadilan dan pemerataan.",
    "Siswa dari luar daerah bisa mendaftar dengan syarat tertentu.",
    "Beberapa sekolah menyediakan jalur khusus untuk difabel.",
    "Nilai rapor semester tertentu bisa menjadi pertimbangan.",
    "PPDB tidak memungut biaya pendaftaran.",
    "Informasi resmi PPDB dapat diakses di website dinas pendidikan.",
    "Pastikan data yang diinput saat pendaftaran benar dan valid.",
    "Jika ada kendala teknis, hubungi helpdesk PPDB setempat.",
    "Setelah diterima, siswa akan mengikuti masa orientasi.",
    "PPDB bertujuan untuk pemerataan akses pendidikan."
]

def chatbot_response(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ["jalur", "zonasi", "afirmasi", "prestasi", "perpindahan"]):
        return "Terdapat beberapa jalur PPDB: zonasi, afirmasi, prestasi, dan perpindahan tugas orang tua."
    elif "syarat" in user_input:
        return "Syarat umum: ijazah, KK, akta kelahiran, dan KTP orang tua."
    elif "daftar ulang" in user_input:
        return "Jika diterima, lakukan daftar ulang di sekolah tujuan agar status diterima tidak gugur."
    elif "kuota" in user_input:
        return "Setiap sekolah memiliki kuota masing-masing untuk tiap jalur."
    elif "website" in user_input or "info" in user_input:
        return "Informasi resmi PPDB dapat diakses di website dinas pendidikan setempat."
    elif "biaya" in user_input:
        return "PPDB tidak memungut biaya pendaftaran."
    elif "hasil" in user_input or "pengumuman" in user_input:
        return "Pengumuman hasil seleksi PPDB dilakukan secara online."
    elif "orientasi" in user_input:
        return "Setelah diterima, siswa akan mengikuti masa orientasi di sekolah."
    elif "difabel" in user_input:
        return "Beberapa sekolah menyediakan jalur khusus untuk difabel."
    elif "nilai" in user_input:
        return "Nilai rapor semester tertentu bisa menjadi pertimbangan jalur prestasi."
    elif "sanggah" in user_input:
        return "Orang tua dapat mengajukan sanggahan jika ada kesalahan data."
    elif "bantuan" in user_input or "helpdesk" in user_input:
        return "Jika ada kendala teknis, hubungi helpdesk PPDB setempat."
    elif "tujuan" in user_input:
        return "Siswa dapat memilih lebih dari satu sekolah tujuan."
    elif "luar daerah" in user_input:
        return "Siswa dari luar daerah bisa mendaftar dengan syarat tertentu."
    elif "jadwal" in user_input or "waktu" in user_input:
        return "Pendaftaran PPDB biasanya dibuka pertengahan tahun ajaran."
    elif "transparan" in user_input:
        return "PPDB transparan dan dapat dipantau secara daring."
    elif "aturan" in user_input:
        return "Setiap daerah memiliki aturan PPDB yang berbeda."
    elif "pemerataan" in user_input:
        return "PPDB bertujuan untuk pemerataan akses pendidikan."
    elif "favorit" in user_input:
        return "Beberapa sekolah favorit memiliki persaingan ketat."
    elif "dokumen" in user_input:
        return "Dokumen yang sering dibutuhkan: KK, Akta Kelahiran, dan KTP orang tua."
    elif "pendaftaran" in user_input:
        return "Pendaftaran PPDB biasanya dilakukan secara online."
    elif "keluarga kurang mampu" in user_input:
        return "Jalur afirmasi untuk siswa dari keluarga kurang mampu."
    elif "asn" in user_input or "pindah tugas" in user_input:
        return "Jalur perpindahan tugas untuk anak ASN yang pindah tugas."
    elif "rapor" in user_input:
        return "Nilai rapor semester tertentu bisa menjadi pertimbangan jalur prestasi."
    elif "verifikasi" in user_input:
        return "Pastikan data yang diinput saat pendaftaran benar dan valid."
    elif "kuota" in user_input:
        return "Setiap sekolah memiliki kuota masing-masing untuk tiap jalur."
    elif "online" in user_input:
        return "PPDB biasanya dilakukan secara online di banyak daerah."
    elif "pengumuman" in user_input:
        return "Pengumuman hasil seleksi PPDB dilakukan secara online."
    elif "daftar" in user_input:
        return "Jika diterima, siswa wajib melakukan daftar ulang di sekolah tujuan."
    else:
        import random
        return random.choice(ppdb_knowledge)

st.title("Chatbot PPDB Sekolah")
st.write("Selamat datang di Chatbot PPDB! Silakan ajukan pertanyaan seputar Penerimaan Peserta Didik Baru.")

if 'history' not in st.session_state:
    st.session_state['history'] = []

user_input = st.text_input("Anda:")
if st.button("Kirim"):
    if user_input:
        response = chatbot_response(user_input)
        st.session_state['history'].append((user_input, response))

if st.session_state['history']:
    st.write("## Riwayat Percakapan")
    for i, (q, a) in enumerate(st.session_state['history']):
        st.markdown(f"**Anda:** {q}")
        st.markdown(f"**Bot:** {a}")
