import '../style/DataInfo.css'

function DataInfo({ data }) {
    
    let tableRows = []

    for (const name in data) {

        let value = String(data[name][0])
        const dataType = data[name][1]

        if (value == 'true' && dataType == 'loģiskais') {
            value = 'patiess'
        } else if (value == 'false' && dataType == 'loģiskais') {
            value = 'nepatiess'
        }

        tableRows.push(
            <tr key={name}>
                <td>{name}</td>
                <td>{value}</td>
                <td>{dataType}</td>
            </tr>
        )
    }

    return (
        <main className='DataInfo'>
            <table>
                <thead>
                    <tr>
                        <th>Nosaukums</th>
                        <th>Vērtība</th>
                        <th>Datu tips</th>
                    </tr>
                </thead>
                <tbody>
                    {tableRows}
                </tbody>
            </table>
        </main>
    )
}

export default DataInfo