import '../../style/TutorialSection.css'

function Comparison() {

    const code1 = 'mainigais skaitlis = 5' + '\n' + 'ja skaitlis vienads 5 tad' + '\n' + '    printet("Skaitlis ir 5")' + '\n' + 'beigas'
    const code2 = 'mainigais temperatura = 20' + '\n' + 'ja temperatura lielaks 25 tad' + '\n' + '    printet("Ir karsts")' + '\n' + 'citadi ja temperatura vismaz 15 tad' + '\n' + '    printet("Ir silts")' + '\n' + 'citadi' + '\n' + '    printet("Ir vēss")' + '\n' + 'beigas'
    const code3 = 'mainigais skaitlis = 1' + '\n' + 'ja skaitlis vismaz 0 tad' + '\n' + '    ja (skaitlis atlikums 2 vienads 0) un (skaitlis - 2 nevienads 0) tad' + '\n' + '        printet("Pozitīvs pāra skaitlis")' + '\n' + '    citadi' + '\n' + '        printet("Pozitīvs nepāra skaitlis")' + '\n' + '    beigas' + '\n' + 'beigas'

    return (
        <main className='Content'>
            <h2>Salīdzināšanas bloki</h2>

            <div className='TutorialArticle'>

                <p>
                    Programmas pseidokodā <b>ja</b> bloku izmanto, lai konkrētas komandas izpildītu tikai tad, 
                    ja konkrētais uzrakstītais nosacījums ir patiess.
                    Nosacījuma beigās jāraksta atslēgvārds <b>tad</b>, bet salīdzināšanas zaru noslēdz ar 
                    atslēgvārdu <b>beigas</b>.
                </p>

                <h3>Ja bloks</h3>
                <p>
                    Pēc atslēgvārda <b>ja</b> jāuzraksta konkrēts nosacījums. Ja šis nosacījums ir patiess,
                    tad programmai atļauj nolasīt um izpilda visas komandas līdz pat ja bloka beigām. 
                    Ja konkrētais nosacījums ir nepatiess, tad programma izlaiž ja blokā atrodamās komandas 
                    un atsāk nākošā rindā pēc ja bloka.
                </p>

                <div className='codeTextArea'>
                    {code1}
                </div>

                <p>
                    Tā kā <b>skaitlis</b> ir vienāds ar 5, konsolē tiks izvadīts teksts <b>Skaitlis ir 5</b>.
                </p>

                <p>
                    Atceries, ka ja mainīgie tiek definēti bloka iekšpusē, tad pēc bloka izpildes, tiek dzēsti.
                </p>

                <h3>Citādi ja un citādi</h3>
                <p>
                    Ja nepieciešams pārbaudīt vairākus variantus, pēc pirmā <b>ja</b> bloka var izmantot <b>citadi ja</b>.
                    Tas nozīmē to, ka situācijā ja <b>ja</b> bloka nosacījums neatbilst, tad programma 
                    skatās <b>citadi ja</b> bloku nosacījumus.
                    Ja neviens no nosacījumiem nav patiess, tiek izpildīts <b>citadi</b> bloks.
                    Vienā zaru virknē tiek izpildīts tikai tas bloks, kas pirmais atbilst nosacījumiem.
                </p>

                <div className='codeTextArea'>
                    {code2}
                </div>

                <p>
                    Šajā piemērā temperatūra ir 20, tāpēc tiks izpildīts <b>citadi ja</b> zars un konsolē parādīsies
                    teksts <b>Ir silts</b>.
                </p>

                <h3>Ligzdoti ja bloki</h3>
                <p>
                    Vienu <b>ja</b> zaru var ielikt cita <b>ja</b> zara iekšpusē.
                    Katram atvērtam zaram nepieciešams savs <b>beigas</b> atslēgvārds.
                </p>

                <div className='codeTextArea'>
                    {code3}
                </div>

                <p>
                    Vispirms tiek pārbaudīts, vai skaitlis ir pozitīvs. Pēc tam iekšējais bloks pārbauda,
                    vai skaitļa dalīšanas atlikums ar 2 ir 0 un vai skaitlis nav 2, ja ir tad 
                    izprintē <b>Pozitīvs pāra skaitlis</b>, bet ja nav tad izprintē <b>Pozitīvs nepāra skaitlis</b>.
                </p>
            </div>
        </main>
    )
}

export default Comparison