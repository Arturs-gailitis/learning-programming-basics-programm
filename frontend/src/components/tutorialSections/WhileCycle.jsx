import '../../style/TutorialSection.css'

function WhileCycle() {

    const code1 = 'mainigais i = 1' + '\n' + 'kamer i mazaks 10 tad' + '\n' + '    printet(i)' + '\n' + '    i = i + 1' + '\n' + 'beigas'
    const code2 = 'mainigais i = 0' + '\n' + 'kamer i mazaks 10 tad' + '\n' + '    i = i + 1' + '\n' + '    ja i vienads 3 tad' + '\n' + '        nakamais' + '\n' + '    citadi ja i vienads 5 tad' + '\n' + '        beidz' + '\n' + '    beigas' + '\n' + '    printet(i)' + '\n' + 'beigas'
 
    return (
        <main className='Content'>
            <h2>Atkārtošanas bloks ar nezināmu robežu</h2>

            <div className='TutorialArticle'>

                <p>
                    Pseidokodā <b>kamer</b> ciklu izmanto, lai komandas atkārtotu tik ilgi, kamēr nosacījums ir patiess.
                    Tas nozīmē, ka rakstot pseidokodu, tajā momentā, nezin cik daudz reizes tas atkārtosies. 
                </p>

                <h3>Kamer cikla izveidošana</h3>
                <p>
                    Cikla pašā sākumā jāuzraksta atslēgvārds <b>kamer</b>.
                    Tad seko nosacījums un pēc tam rindas beigās ir jābūt atslēgvārdam <b>tad</b>.
                    Cikla rindas beigās jāraksta <b>beigas</b>.
                </p>

                <div className='codeTextArea'>
                    {code1}
                </div>

                <p>
                    Cikls izvadīs skaitļus no 1 līdz 9. Pēc tam, kad <b>i</b> ir ķļuvis par 6,
                    cikla nodefinētais nosacījums vairs nebūs patiess un cikls automātiski beigsies.
                </p>

                <p>
                    Šaja cikla veidā obligāti ir jāmaina nosacījuma mainīgais, jo savādāk cikla darbība būs bezgalīga
                    un nevarēs to pabeigt.
                </p>

                <h3>Nākamās iterācijas izlaišana vai piespiedus apturēšana</h3>
                <p>
                    Tā pat kā ar iepriekšējo cikla veidu, tad arī šim ciklam 
                    var ar atslēgvārdiem <b>nakamais</b> un <b>beigt</b> manuāli sākt nākamo cikla iterāciju
                    vai pārtraukt ciklu pat ja nosacījums ir patiess
                    Tos bieži vien izmanto kopā ar <b>ja</b> bloku.
                </p>

                <div className='codeTextArea'>
                    {code2}
                </div>

                <p>
                    Kad <b>i</b> kļūst par 3, tiek izpildīts <b>nakamais</b>, tāpēc skaitlis 3 netiek izvadīts.
                    Pēc tam cikls turpinās ar nākamo iterāciju līdz nokļūst par 5.
                    Tad cikls, piespiedus kārtā, beidzās.
                </p>

            </div>
        </main>
    )
}

export default WhileCycle