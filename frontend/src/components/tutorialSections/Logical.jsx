import '../../style/TutorialSection.css'

function Logical() {

    const code1 = 'mainigais pareizs = patiess' + '\n' + 'mainigais nepareizs = nepatiess'
    const code2 = 'mainigais a = patiess un patiess' + '\n' + 'mainigais b = nepatiess vai patiess'
    const code3 = 'mainigais l = 11.1 lielaks 11' + '\n' + 'mainigais m = 0.9 mazaks 1'

    return (
        <main className='Content'>
            <h2>Loģiskās operācijas</h2>

            <div className='TutorialArticle'>

                <p>
                    Loģiskās operācijas tiek izmantotas, lai pārbaudītu, vai kāds no nosacījumiem ir pateiss vai nepatiess.
                    Šīs programmas pseidokodā lōģiskās vērtības ir tikai 2: <b>patiess</b> un <b>nepatiess</b>.
                </p>

                <h3>Loģiskās vērtības</h3>

                <p>
                    Loģiskās vērtības var glabātis tāpat kā teksta vai skaitļu vērtības.
                    Vērtība <b>patiess</b> nozīmē ka kaut kāds salīdzinājums bijis patiess, bet
                    vērtība <b>nepatiess</b> - salīdzinājums bijis nepatiess.
                </p>

                <div className='codeTextArea'>
                    {code1}
                </div>

                <h3>Loģiskās darbības ar un, vai </h3>

                <p>
                    Atslēgvārds <b>un</b> atgriezīs vērtību <b>patiess</b>, ja salīdzinājumi abās pusēs būs patiesi,
                    Atslēgvārds <b>vai</b> atgriezīs vērtību <b>patiess</b>, ja vizmaz viens no salīdzinājumiem 
                    abās pusēs būs patiess.
                </p>

                <div className='codeTextArea'>
                    {code2}
                </div>

                <p>
                    Mainīgā <b>a</b> vērtība būs <b>patiess</b>, jo abi salīdzinājumi ir patiesi.
                    Mainīgā <b>b</b> vērtība arī būs <b>patiess</b>, jo vismaz viens no salīdzinājumiem ir patiess.
                </p>

                <h3>Vērtību salīdzināšana</h3>

                <p>
                    Lai salīdzinātu divas vērtības, var izmantot šādus atslēgvārdus:
                </p>
                <ul>
                    <li>
                        <b>vienads</b> pārbauda, vai abas dotās vērtības ir vienādas; 
                        <div className='codeTextArea'>{'mainigais x = 3 vienads 3'}</div>
                    </li>
                    <li>
                        <b>nevienads</b> pārbauda, vai abas dotās vērtības atšķirās;
                        <div className='codeTextArea'>{'mainigais y = 3 nevienads 8'}</div>
                    </li>
                    <li>
                        <b>lielaks</b> un <b> mazaks</b> pārbauda, vai kreisā vērtība ir lielāka vai mazāka nekā labā vērtība;
                        <div className='codeTextArea'>{code3}</div>
                    </li>
                    <li>
                        <b>vismaz</b> pārbauda, vai kreisā vērtība ir vai nu vienāda vai lielāka nekā labā vērtība;
                        <div className='codeTextArea'>{'mainigais minimālais = 19 vismaz 19'}</div>
                    </li>
                    <li>
                        <b>neparsniedz</b> pārbauda vai kreisā vērtība ir vai nu mazāka vai vienāda nekā labā vērtība.
                        <div className='codeTextArea'>{'mainigais liels = 14 neparsniedz 20'}</div>
                    </li>
                </ul>

                <h3>Vairāku salīdzinājuu izmantošana</h3>

                <p>
                    Lai vairākus salīdzinājumus apvienotu kopā, tiek izmantoti <b>un</b>, <b>vai</b> atslēgvārdi.
                    Tāpat kā matemātiskajās operācijās, arī šeit ar iekavām norāda, kurš salīdzinājums būs pirmais.
                </p>

                <div className='codeTextArea'>
                    {'mainigais rezultats = (5 lielaks 3) un (2 mazaks 4)'}
                </div>

                <p>
                    Šajā situācijā sākumā salīdzinās kas atrodās abās iekavās un tad abus salīdzinās ar <b>un</b> atlsēgvārdu.
                </p>
            </div>
        </main>
    )
}

export default Logical