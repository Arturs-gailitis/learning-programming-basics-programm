import '../../style/TutorialSection.css'

function ForCycle() {

    const code1 = 'cikls i no 1 lidz 10:' + '\n' + '    printet(i)' + '\n' + 'beigas'
    const code2 = 'mainigais rezultāts = 0' + '\n' + 'cikls i no 1 lidz 10:' + '\n' + '    rezultāts = rezultāts + (i + 1)' + '\n' + 'beigas' + '\n' + 'printet(rezultāts)'
    const code3 = 'mainigais sakums = 1' + '\n' + 'mainigais beigas = 6' + '\n' + 'cikls i no sakums lidz beigas:' + '\n' + '    printet(i)' + '\n' + 'beigas'
    const code4 = 'cikls i no 1 lidz 10:' + '\n' + '    ja i atlikums 2 nevienads 0 tad' + '\n' + '        nakamais' + '\n' + '    beigas' + '\n' + '    printet(i)' + '\n' + 'beigas'
    const code5 = 'cikls i no 1 lidz 10:' + '\n' + '    ja i vienads 5 tad' + '\n' + '        beidz' + '\n' + '    beigas' + '\n' + '    printet(i)' + '\n' + 'beigas'
    const code6 = 'cikls i no 1 lidz 2:' + '\n' + '    cikls j no 1 lidz 3:' + '\n' + '        mainigais k = i + j' + '\n' + '        printet(k)' + '\n' + '    beigas' + '\n' + 'beigas'

    return (
        <main className='Content'>
            <h2>Atkārtošanas bloks ar zināmu robežu</h2>

            <div className='TutorialArticle'>

                <p>
                    Programmas pseidokodā ar atlsēgvārdu <b>cikls</b> izmanto, lai vienas un tās pašas komandas 
                    izpildītu noteiktas reizes.
                    Šo cikla veidu izmanto tad, ja jau iepriekš ir zināms, cik daudzas reizes jāatkārto darbības.
                    Tā pat kā ar citiem blokiem, ja izveido ciklā mainīgo, tad pēc cikla tiks izdzēsts.
                </p>

                <h3>Cikla izveidošana</h3>
                <p>
                    Šī cikla veida sākumā jāuzraksta atslēgvārds <b>cikls</b>, iterācijas lokālā mainīgā nosaukums,
                    atslēgvārds <b>no</b>, sākuma robeža, atslēgvārds <b>lidz</b> un beigu robeža.
                    Rindas beigās jāraksta kols, bet ciklu noslēdz ar atslēgvārdu <b>beigas</b>.
                </p>

                <div className='codeTextArea'>
                    {code1}
                </div>

                <p>
                    Šajā dotajā piemērā cikls izpildīsies 10 reizes. 
                    Lokālais mainīgais <b>i</b> pēc kārtas iegūs vērtības no 1 līdz 10, 
                    un konsolē tiks izvadīts katrs no šiem skaitļiem.
                </p>

                <h3>Lokālās iterācijas mainīgā izmantošana</h3>
                <p>
                    Lokālās iterācijas mainīgo var izmantot paša cikla iekšienē, piemēram, lai veiktu aprēķinus vai salīddzināšanu.
                    Cikla beigās šis mainīgais tiek izdzēsts, tāpēc ārpus cikla tas vairs tālāk nebūs pieejams.
                </p>

                <div className='codeTextArea'>
                    {code2}
                </div>

                <p>
                    Cikls saskaitīs skaitļus no 1 līdz 10 un pieskaitīs klāt vēl 10. Pēc cikla mainīgā <b>summa</b> vērtība būs 65.
                </p>

                <h3>Dažādu mainīgo izmantošana cikla robežās</h3>
                <p>
                    Cikla sākuma un beigu robežu var norādīt arī ar iepriekš nodefinētajiem mainīgajiem.
                    Cikls tiks izpildīsies tā pat, kā tas būtu uzrakstīts ar statiskām robežām.
                </p>

                <div className='codeTextArea'>
                    {code3}
                </div>

                <p>
                    Šajā piemērā mainīgais <b>skaitlis</b> iegūs vērtības no 1 līdz 6.
                    Beigu vērtība tiek iekļauta ciklā.
                </p>

                <h3>Nākamās iterācijas izlaišana vai cikla pārtraukšana</h3>
                <p>
                    Lai izlaistu pašreizējo palaisto iterāciju un pārietu pie nākamās, jāizmanto atslēgvārds <b>nakamais</b>.
                    To var bieži vien izmantot, piemēram, kopā ar <b>ja</b> bloku.
                </p>

                <div className='codeTextArea'>
                    {code4}
                </div>

                <p>
                    Kad <b>i</b> ir nepāra skaitlis, tiek izpildīts <b>nakamais</b>, tāpēc konkrētais nepāra skaitlis
                    netiek izvadīts.
                    Pārējās iterācijas turpinās kā parasti.
                </p>

                <p>
                    Lai piespiedus kārtā atceltu ciklu, tiek izmantots atslēgvārds <b>beidz</b>.
                    To var bieži vien izmantot, piemēram, kopā ar <b>ja</b> bloku.
                </p>

                <div className='codeTextArea'>
                    {code5}
                </div>

                <p>
                    Kad <b>i</b> ir kļūst par 5, tiek izpildīts <b>beidz</b>, tāpēc cikls beidzās ātrāk.
                </p>

                <h3>Ligzdoti cikli</h3>
                <p>
                    Vienu <b>cikls</b> bloku var ievietot cita cikla iekšpusē.
                    Protams katram ciklam nepieciešams savs <b>beigas</b> atslēgvārds, lai beigtu katru <b>cikls</b> bloku.
                </p>

                <div className='codeTextArea'>
                    {code6}
                </div>

                <p>
                    Ārējais cikls izpildīsies divas reizes, bet iekšējais cikls katrā ārējā cikla iterācijā izpildīsies vēl trīs reizes.
                </p>
            </div>
        </main>
    )
}

export default ForCycle