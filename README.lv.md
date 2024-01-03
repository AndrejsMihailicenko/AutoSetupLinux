# AutoSetupLinux
*Lasīt citās valodās: [English](README.md).*

## Kas ir AutoSetupLinux?
AutoSetupLinux ir vienkāršs Python skripts. Es izstrādāju šo programmu priekš Rīgas Tehniskās Universitātes kursa DIP225 'Lietojumprogrammatūras automatizēšanas rīki'. Kursa ietvāros jāizveido automatizāciju priekš kādas no ikdienas uzdēvumiem. Mana idēja, ir atvieglot virtuālās mašīnas vai resursdatora Linux sistēmas pēc-instalēšanas soļus. Katru reizi veidojot jauno virtuālo mašīnu, programmatūra kuru es instalēju ir apmēram vienāda. Tāpēc, ir vērts izstrādāt scriptu, kas atvieglos un samazinās laiku vēltīto uz komandas ievādi.<br>

**Es rekomendēju izmantot scriptu Fedora 38 sistēmas iestatīšanai!**

## Kas ir nepieciešams?
- Python 3.
- Python 3 `pip`.
- `bs4` (BeautifulSoup), `distro`, `requests` bibliotēkas.
- Interneta pieslēgums.
- Spēja izmantot sudo komandas vai piekļuvi root tiesībām.

## Bibliotēkas izmantošanas pamatojums
- bs4 -> izmanto priekš web scrapping, lai atvērt Oracle tīmekļa lapu un mēklēt HTML koda linku uz instalēšanu.
- subprocess -> izmanto, lai ievadīt sistēmas komandes termināla
- distro -> linuks izplātīšanas vērsijas noteikšanai
- sys -> izmanto, priekš sistēmas funkcijas izmantošanas.Piemēram sys.exit()
- requests -> izmanto, lai izpildīt HTTP pieprasījumus

## Kā Iestatīt un Lietot
1. Klonējiet GitHub repozitoriju uz jūsu datoru.
2. Ienāciet direktorīja kurā klonēts projekts.
2. **Palaidiet Skriptu**

```bash
git clone https://github.com/AndrejsMihailicenko/AutoSetupLinux.git
cd AutoSetupLinux/
python3 setup.py
```
## Scripta darbība
- **os_detector**: Vispirms skripts noskaidro, kādu Linux sistēmu jūs izmantojat. Šobrīd skripts strādā ar RHEL(Fedora, CentOS, Red Hat Enterprise Linux) bāzētiem distro. Ja operētājsistēma nav atpazīta, izbeidz izpildi un izvada paziņojumu par nepieļaujamu sistēmu.
- **install_libraries**: Funkcijā instalē visas Python bibliotēkas, kas uzskaitītas requirements.txt.
- **system_update**: Atjauno sistēmas pakotnes izmantojot norādīto pakotēs pārvaldītāju (piemēram, "dnf" vai "apt").
Izmanto subprocess.run funkciju, lai izpildītu komandas sistēmas procesā, piemēram, 'sudo dnf update -y'.
- **read_packages**: Nolasa programmu sarakstu no "packages.csv" faila, izlaižot pirmo rindiņu (virsrakstu).
Katru programmu nosaukumu pievieno sarakstam apps_list.
- **Instalē JDK**: Visbeidzot, skripts iegūst Oracle Java Development Kit (JDK) lejupielādes saiti no Oracle mājaslapas, izmantojot requests un bs4.
Atkarībā no operētājsistēmas un pieejamās JDK versijas saņem konkrēto lejupielādes saiti un faila nosaukumu.
Lejupielādē JDK un instalē to, izmantojot atbilstošo komandu (sudo dnf install vai sudo dpkg -i).
- **apps_installation**: Funkcija instalē visas programmas no saraksta apps_list, izmantojot norādīto pakotēs pārvaldītāju.
Katru programmu nosaukumu padod kā argumentu sistēmas komandai, piemēram, sudo dnf install.