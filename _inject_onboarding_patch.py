# -*- coding: utf-8 -*-
"""Inject applyCrmOnboardingEnhancements + wiring into different._AIplatform_V4.0.html"""
from pathlib import Path

PATH = Path(__file__).resolve().parent / "different._AIplatform_V4.0.html"

APPLY_FN = r'''
  function applyCrmOnboardingEnhancements(html) {
    var h = html;
    if (h.indexOf("CRM onboarding wealth goals v1") !== -1) return h;

    h = h.replace(
      "<script src=\"https://cdn.jsdelivr.net/npm/chart.js@4\"></script>",
      "<script src=\"https://cdn.jsdelivr.net/npm/chart.js@4\"></script>" +
      "<script src=\"https://cdn.jsdelivr.net/npm/echarts@5.5.1/dist/echarts.min.js\"></script>"
    );

    h = h.replace(
      "</style>",
      "/* CRM onboarding wealth goals v1 */" +
      ".onb-wealth-wrap{margin:0 0 22px;padding:18px;border-radius:16px;border:1px solid var(--border);" +
      "background:linear-gradient(135deg,rgba(172,11,227,.1),rgba(255,78,80,.07));box-shadow:var(--glow-frame)}" +
      ".onb-wealth-head{display:flex;align-items:flex-start;justify-content:space-between;gap:14px;margin-bottom:12px}" +
      ".onb-wealth-titles .onb-kicker{font-size:.68rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--text-muted)}" +
      ".onb-wealth-titles .onb-title{font-size:1.08rem;font-weight:700;margin-top:4px;color:var(--text)}" +
      ".onb-wealth-titles .onb-hint{font-size:.78rem;color:var(--text-sec);margin-top:6px;line-height:1.45;max-width:54ch}" +
      ".onb-wealth-deco{width:58px;height:58px;flex-shrink:0;opacity:.95}" +
      ".onb-wealth-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(152px,1fr));gap:10px}" +
      ".onb-wealth-chip{position:relative;display:block;width:100%;text-align:left;border:1px solid var(--border);border-radius:14px;" +
      "padding:12px 12px 12px 46px;cursor:pointer;background:var(--surface-alt);color:inherit;" +
      "transition:transform .16s ease,box-shadow .16s ease,border-color .16s ease}" +
      ".onb-wealth-chip:hover{transform:translateY(-2px);box-shadow:0 10px 28px rgba(0,0,0,.35);border-color:rgba(172,11,227,.45)}" +
      ".onb-wealth-chip.selected{border-color:rgba(172,11,227,.8);box-shadow:0 0 0 1px rgba(172,11,227,.4),0 12px 32px rgba(157,0,255,.2)}" +
      ".onb-wealth-chip .onb-ico{position:absolute;left:10px;top:50%;transform:translateY(-50%);width:30px;height:30px}" +
      ".onb-wealth-chip .onb-lbl{font-size:.83rem;font-weight:600;line-height:1.25;color:var(--text)}" +
      ".onb-wealth-chip .onb-sub{font-size:.68rem;color:var(--text-muted);margin-top:3px;line-height:1.3}" +
      ".onb-warn{display:none;margin-top:10px;padding:8px 12px;border-radius:10px;font-size:.75rem;color:#fecaca;" +
      "background:rgba(234,75,59,.12);border:1px solid rgba(234,75,59,.35)}" +
      ".onb-warn.visible{display:block}" +
      ".onb-asset-wrap{margin:0 0 20px;padding:18px;border-radius:16px;border:1px solid var(--border);background:var(--surface)}" +
      ".onb-asset-head{margin-bottom:12px}" +
      ".onb-asset-head .onb-kicker{font-size:.68rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--text-muted)}" +
      ".onb-asset-head .onb-title{font-size:1.05rem;font-weight:700;margin-top:4px}" +
      ".onb-asset-head .onb-hint{font-size:.78rem;color:var(--text-sec);margin-top:6px;line-height:1.45}" +
      ".onb-asset-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}" +
      "@media(max-width:980px){.onb-asset-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}" +
      ".onb-asset-chip{display:block;width:100%;border:1px solid var(--border);border-radius:16px;padding:14px 10px;text-align:center;" +
      "cursor:pointer;background:var(--surface-alt);color:inherit;transition:transform .16s ease,box-shadow .16s ease,border-color .16s ease}" +
      ".onb-asset-chip:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(0,0,0,.32)}" +
      ".onb-asset-chip.selected{border-color:rgba(52,211,153,.7);box-shadow:0 0 0 1px rgba(52,211,153,.35)}" +
      ".onb-asset-chip svg{width:42px;height:42px;margin:0 auto 8px;display:block}" +
      ".onb-asset-chip .onb-lbl{font-size:.8rem;font-weight:700}" +
      ".onb-asset-chip .onb-sub{font-size:.65rem;color:var(--text-muted);margin-top:4px;line-height:1.25}" +
      ".onb-treemap-wrap{margin-top:14px;padding:18px;border-radius:16px;border:1px solid var(--border);" +
      "background:radial-gradient(900px 380px at 12% -30%,rgba(172,11,227,.14),transparent 50%),var(--surface)}" +
      ".onb-treemap-head{display:flex;align-items:baseline;justify-content:space-between;gap:12px;margin-bottom:12px;flex-wrap:wrap}" +
      ".onb-treemap-head .onb-title{font-size:1.06rem;font-weight:700}" +
      ".onb-treemap-head .onb-sub{font-size:.78rem;color:var(--text-sec);max-width:46ch;line-height:1.45}" +
      ".onb-treemap-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}" +
      "@media(max-width:1180px){.onb-treemap-grid{grid-template-columns:1fr}}" +
      ".onb-tm-card{border-radius:14px;border:1px solid var(--border);background:var(--surface-alt);padding:10px 10px 8px;" +
      "display:flex;flex-direction:column;min-height:248px}" +
      ".onb-tm-card .onb-tm-hd{font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);" +
      "margin:2px 4px 6px}" +
      ".onb-tm-chart{flex:1;min-height:208px}" +
      ".onb-tm-foot{margin-top:8px;font-size:.65rem;line-height:1.45;color:var(--text-muted);padding:0 4px}" +
      "html[data-theme=\"light\"] .onb-wealth-wrap{background:linear-gradient(135deg,rgba(172,11,227,.07),rgba(255,78,80,.05))}" +
      "</style>"
    );

    h = h.replace(
      "const FUNDS=[\\n  {name:'zCapital-Swiss Dividend Fund A CHF',cat:'Growth',cls:'cat-growth',pct:{cautious:6,moderate:12,daredevil:16}},\\n  {name:'AAE Global Strategy Fund CHF',cat:'Growth',cls:'cat-growth',pct:{cautious:5,moderate:10,daredevil:14}},\\n  {name:'Barings ASEAN Frontiers Fund I CHF',cat:'Growth',cls:'cat-growth',pct:{cautious:4,moderate:8,daredevil:10}},\\n  {name:'Bakersteel Precious Metals Fund A CHF',cat:'Growth',cls:'cat-growth',pct:{cautious:3,moderate:5,daredevil:7}},\\n  {name:'EM Corporate IG Bond Fund BH CHF',cat:'Income',cls:'cat-income',pct:{cautious:15,moderate:12,daredevil:8}},\\n  {name:'Global High Yield Bond Fund P-HDG CHF',cat:'Income',cls:'cat-income',pct:{cautious:12,moderate:10,daredevil:7}},\\n  {name:'Alpina Best Select Portfolio CHF',cat:'Income',cls:'cat-income',pct:{cautious:13,moderate:10,daredevil:7}},\\n  {name:'PCP Convex Diversification Hedged CHF',cat:'Stabilization',cls:'cat-stab',pct:{cautious:12,moderate:10,daredevil:11}},\\n  {name:'Dominice Swiss Property Fund CHF',cat:'Stabilization',cls:'cat-stab',pct:{cautious:10,moderate:8,daredevil:7}},\\n  {name:'ZKB Gold ETF',cat:'Protection',cls:'cat-prot',pct:{cautious:12,moderate:8,daredevil:6}},\\n  {name:'LGT Sustainable Money Market Fund CHF',cat:'Protection',cls:'cat-prot',pct:{cautious:8,moderate:7,daredevil:7}}\\n];",
      "const FUNDS=[\\n  {name:'zCapital-Swiss Dividend Fund A CHF',cat:'Growth',cls:'cat-growth',pct:{cautious:6,moderate:12,daredevil:16},tmAc:'equities',tmReg:'switzerland',tmInd:'financials',prodType:'Equity'},\\n  {name:'AAE Global Strategy Fund CHF',cat:'Growth',cls:'cat-growth',pct:{cautious:5,moderate:10,daredevil:14},tmAc:'multi',tmReg:'global',tmInd:'diversified',prodType:'Equity'},\\n  {name:'Barings ASEAN Frontiers Fund I CHF',cat:'Growth',cls:'cat-growth',pct:{cautious:4,moderate:8,daredevil:10},tmAc:'equities',tmReg:'asia',tmInd:'technology',prodType:'Equity'},\\n  {name:'Bakersteel Precious Metals Fund A CHF',cat:'Growth',cls:'cat-growth',pct:{cautious:3,moderate:5,daredevil:7},tmAc:'commodities',tmReg:'global',tmInd:'materials',prodType:'Equity'},\\n  {name:'EM Corporate IG Bond Fund BH CHF',cat:'Income',cls:'cat-income',pct:{cautious:15,moderate:12,daredevil:8},tmAc:'bonds',tmReg:'emerging',tmInd:'financials',prodType:'Fixed Income'},\\n  {name:'Global High Yield Bond Fund P-HDG CHF',cat:'Income',cls:'cat-income',pct:{cautious:12,moderate:10,daredevil:7},tmAc:'bonds',tmReg:'global',tmInd:'financials',prodType:'Fixed Income'},\\n  {name:'Alpina Best Select Portfolio CHF',cat:'Income',cls:'cat-income',pct:{cautious:13,moderate:10,daredevil:7},tmAc:'bonds',tmReg:'europe',tmInd:'diversified',prodType:'Fixed Income'},\\n  {name:'PCP Convex Diversification Hedged CHF',cat:'Stabilization',cls:'cat-stab',pct:{cautious:12,moderate:10,daredevil:11},tmAc:'bonds',tmReg:'global',tmInd:'financials',prodType:'Fixed Income'},\\n  {name:'Dominice Swiss Property Fund CHF',cat:'Stabilization',cls:'cat-stab',pct:{cautious:10,moderate:8,daredevil:7},tmAc:'property',tmReg:'switzerland',tmInd:'real_estate',prodType:'Real Estate'},\\n  {name:'ZKB Gold ETF',cat:'Protection',cls:'cat-prot',pct:{cautious:12,moderate:8,daredevil:6},tmAc:'commodities',tmReg:'global',tmInd:'materials',prodType:'Equity'},\\n  {name:'LGT Sustainable Money Market Fund CHF',cat:'Protection',cls:'cat-prot',pct:{cautious:8,moderate:7,daredevil:7},tmAc:'cash',tmReg:'switzerland',tmInd:'diversified',prodType:'Cash'}\\n];"
    );

    h = h.replace(
      "const INSTRUMENT_CATEGORIES=['Growth','Income','Stabilization','Protection'];",
      "var CRM_ONB_I18N={" +
        "en:{" +
          "wealthKicker:'Wealth planning',wealthTitle:'Start with wealth goals',wealthHint:'Pick one or more life goals — we align liquidity, risk budget and sleeves around them.'," +
          "assetKicker:'Product mix',assetTitle:'Asset type preferences',assetHint:'Same taxonomy as CRM products: Cash, Equity, Fixed Income, Real Estate. Multi-select.'," +
          "wealthRequired:'Please select at least one wealth goal to continue.'," +
          "treemapTitle:'Portfolio distribution',treemapSub:'Weighted by instrument weights in the active allocation bucket'," +
          "treemapAc:'Asset class',treemapReg:'Region',treemapInd:'Industry / sector',treemapDisclaimer:'Illustrative sleeve breakdown from fund metadata; not a forecast of performance.'," +
          "parseCheckPrefs:'Parse customer preferences (risk profile + asset types)'," +
          "goals:{" +
            "property:{title:'Property purchase',sub:'Down payment & Mortgage'}," +
            "retirement:{title:'Retirement',sub:'Income replacement timeline'}," +
            "education:{title:'Children education',sub:'Tuition & milestones'}," +
            "preserve:{title:'Wealth preservation',sub:'Inflation-aware stability'}," +
            "grow:{title:'Wealth growth',sub:'Compounding & equity tilt'}," +
            "parents:{title:'Parent support',sub:'Care & liquidity buffer'}" +
          "}," +
          "assets:{" +
            "cash:{title:'Cash',sub:'Liquidity & money-market'}," +
            "equity:{title:'Equity',sub:'Stocks & growth sleeves'}," +
            "fixed:{title:'Fixed income',sub:'Bonds & carry'}," +
            "re:{title:'Real estate',sub:'Listed & direct property'}" +
          "}" +
        "}," +
        "'zh-CN':{" +
          "wealthKicker:'财富规划',wealthTitle:'先添加财富目标',wealthHint:'选择一个或多个人生目标，我们将据此优化流动性、风险预算与配置结构。'," +
          "assetKicker:'产品偏好',assetTitle:'资产类型偏好',assetHint:'与产品管理一致：现金、股票、固定收益、房地产，可多选。'," +
          "wealthRequired:'请至少选择一个财富目标后再继续。'," +
          "treemapTitle:'组合分布',treemapSub:'按当前所选配置桶内基金的权重统计'," +
          "treemapAc:'资产类别',treemapReg:'地区',treemapInd:'行业',treemapDisclaimer:'基于基金元数据的示意分布，不构成业绩预测。'," +
          "parseCheckPrefs:'解析客户偏好（风险画像与资产类型）'," +
          "goals:{" +
            "property:{title:'房产购置',sub:'首付与按揭节奏'}," +
            "retirement:{title:'退休规划',sub:'现金流与替代率'}," +
            "education:{title:'子女教育',sub:'学费与阶段目标'}," +
            "preserve:{title:'财富保值',sub:'通胀与稳健'}," +
            "grow:{title:'财富增值',sub:'复利与权益暴露'}," +
            "parents:{title:'赡养父母',sub:'照护与备用金'}" +
          "}," +
          "assets:{" +
            "cash:{title:'现金',sub:'流动性 / 货基'}," +
            "equity:{title:'股票 / 权益',sub:'股票与成长类'}," +
            "fixed:{title:'固定收益',sub:'债券与票息'}," +
            "re:{title:'房地产',sub:'直投与地产基金'}" +
          "}" +
        "}," +
        "'zh-TW':{" +
          "wealthKicker:'財富規劃',wealthTitle:'先新增財富目標',wealthHint:'選擇一個或多個目標，據此優化流動性、風險與配置。'," +
          "assetKicker:'產品偏好',assetTitle:'資產類型偏好',assetHint:'與產品類型一致：現金、股票、固定收益、房地產，可多選。'," +
          "wealthRequired:'請至少選擇一個財富目標後再繼續。'," +
          "treemapTitle:'組合分布',treemapSub:'依目前所選桶內基金權重統計'," +
          "treemapAc:'資產類別',treemapReg:'地區',treemapInd:'行業',treemapDisclaimer:'示意分布，不代表績效預測。'," +
          "parseCheckPrefs:'解析客戶偏好（風險與資產類型）'," +
          "goals:{" +
            "property:{title:'房產置業',sub:'首付與按揭節奏'}," +
            "retirement:{title:'退休規劃',sub:'現金流與替代率'}," +
            "education:{title:'子女教育',sub:'學費與里程碑'}," +
            "preserve:{title:'財富保值',sub:'通膨與穩健'}," +
            "grow:{title:'財富增值',sub:'複利與權益'}," +
            "parents:{title:'孝敬父母',sub:'照護與備用金'}" +
          "}," +
          "assets:{" +
            "cash:{title:'現金',sub:'流動性'}," +
            "equity:{title:'股票 / 權益',sub:'成長類'}," +
            "fixed:{title:'固定收益',sub:'債券'}," +
            "re:{title:'房地產',sub:'地產曝險'}" +
          "}" +
        "}," +
        "ja:{" +
          "wealthKicker:'ウェルス',wealthTitle:'まず財富目標',wealthHint:'複数選択可。流動性とリスク設計の起点になります。'," +
          "assetKicker:'資産タイプ',assetTitle:'資産クラス嗜好',assetHint:'Cash / Equity / Fixed Income / Real Estate（複数選択）'," +
          "wealthRequired:'少なくとも1つの目標を選んでください。'," +
          "treemapTitle:'ポートフォリオ分布',treemapSub:'選択中バケットの加重内訳'," +
          "treemapAc:'資産クラス',treemapReg:'地域',treemapInd:'業種',treemapDisclaimer:'参考用の内訳（業績保証ではありません）。'," +
          "parseCheckPrefs:'嗜好（リスク+資産タイプ）を解析'," +
          "goals:{" +
            "property:{title:'不動産購入',sub:'頭金・ローン'}," +
            "retirement:{title:'老後準備',sub:'キャッシュフロー'}," +
            "education:{title:'子女教育',sub:'学費'}," +
            "preserve:{title:'資産保全',sub:'インフレ対策'}," +
            "grow:{title:'資産形成',sub:'複利・株式'}," +
            "parents:{title:'親の扶養',sub:'ケア・準備金'}" +
          "}," +
          "assets:{" +
            "cash:{title:'キャッシュ',sub:'流動性'}," +
            "equity:{title:'株式',sub:'エクイティ'}," +
            "fixed:{title:'債券',sub:'FI'}," +
            "re:{title:'不動産',sub:'RE'}" +
          "}" +
        "}" +
      "};" +
      "var CRM_TM_LABELS={" +
        "en:{ac:{equities:'Equities',bonds:'Bonds',cash:'Cash & equivalents',property:'Real estate',commodities:'Commodities',multi:'Multi-asset'}," +
        "reg:{switzerland:'Switzerland',usa:'United States',uk:'United Kingdom',global:'Global',asia:'Asia Pacific',emerging:'Emerging markets',europe:'Europe'}," +
        "ind:{financials:'Financials',technology:'Information technology',real_estate:'Real estate',materials:'Materials',healthcare:'Healthcare',industrials:'Industrials',consumer:'Consumer',diversified:'Diversified'}}," +
        "'zh-CN':{ac:{equities:'股票',bonds:'债券',cash:'现金',property:'房地产',commodities:'商品',multi:'多资产'}," +
        "reg:{switzerland:'瑞士',usa:'美国',uk:'英国',global:'全球',asia:'亚太',emerging:'新兴市场',europe:'欧洲'}," +
        "ind:{financials:'金融',technology:'信息技术',real_estate:'房地产',materials:'原材料',healthcare:'医疗',industrials:'工业',consumer:'消费',diversified:'综合'}}," +
        "'zh-TW':{ac:{equities:'股票',bonds:'債券',cash:'現金',property:'房地產',commodities:'商品',multi:'多資產'}," +
        "reg:{switzerland:'瑞士',usa:'美國',uk:'英國',global:'全球',asia:'亞太',emerging:'新興市場',europe:'歐洲'}," +
        "ind:{financials:'金融',technology:'資訊科技',real_estate:'房地產',materials:'原物料',healthcare:'醫療',industrials:'工業',consumer:'消費',diversified:'綜合'}}," +
        "ja:{ac:{equities:'株式',bonds:'債券',cash:'現金同等',property:'不動産',commodities:'コモディティ',multi:'マルチアセット'}," +
        "reg:{switzerland:'スイス',usa:'米国',uk:'英国',global:'グローバル',asia:'アジア',emerging:'新興国',europe:'欧州'}," +
        "ind:{financials:'金融',technology:'IT',real_estate:'不動産',materials:'素材',healthcare:'ヘルスケア',industrials:'資本財',consumer:'消費',diversified:'分散'}}" +
      "};" +
      "function crmOnbTt(k){var p=CRM_ONB_I18N[currentLocale]||CRM_ONB_I18N.en;var f=CRM_ONB_I18N.en;return p[k]!==undefined?p[k]:f[k];}" +
      "function crmTmLabel(dim,key){" +
        "var loc=currentLocale==='ja'?'ja':(currentLocale==='zh-CN'?'zh-CN':(currentLocale==='zh-TW'?'zh-TW':'en'));" +
        "var L=CRM_TM_LABELS[loc]||CRM_TM_LABELS.en;var m=L[dim]||{};return m[key]||key;" +
      "}" +
      "function crmRefreshOnbDom(){" +
        "var w=document.getElementById('onb-wealth-wrap');if(!w)return;" +
        "var g=(crmOnbTt('goals')||{});" +
        "w.querySelectorAll('.onb-wealth-chip').forEach(function(chip){" +
          "var id=chip.getAttribute('data-goal');var gg=g[id]||{};" +
          "var l=chip.querySelector('.onb-lbl');var s=chip.querySelector('.onb-sub');" +
          "if(l)l.textContent=gg.title||id;if(s)s.textContent=gg.sub||'';" +
        "});" +
        "var ak=document.getElementById('onb-asset-kicker');if(ak)ak.textContent=crmOnbTt('assetKicker');" +
        "var at=document.getElementById('onb-asset-title');if(at)at.textContent=crmOnbTt('assetTitle');" +
        "var ah=document.getElementById('onb-asset-hint');if(ah)ah.textContent=crmOnbTt('assetHint');" +
        "var ag=(crmOnbTt('assets')||{});" +
        "document.querySelectorAll('.onb-asset-chip').forEach(function(chip){" +
          "var id=chip.getAttribute('data-asset');var a=ag[id]||{};" +
          "var l=chip.querySelector('.onb-lbl');var s=chip.querySelector('.onb-sub');" +
          "if(l)l.textContent=a.title||id;if(s)s.textContent=a.sub||'';" +
        "});" +
        "var wk=document.getElementById('onb-wealth-kicker');if(wk)wk.textContent=crmOnbTt('wealthKicker');" +
        "var wt=document.getElementById('onb-wealth-title');if(wt)wt.textContent=crmOnbTt('wealthTitle');" +
        "var wh=document.getElementById('onb-wealth-hint');if(wh)wh.textContent=crmOnbTt('wealthHint');" +
        "var wr=document.getElementById('onb-wealth-warn');if(wr){wr.textContent=crmOnbTt('wealthRequired');wr.classList.remove('visible');}" +
        "var tm=document.getElementById('onb-treemap-title');if(tm)tm.textContent=crmOnbTt('treemapTitle');" +
        "var ts=document.getElementById('onb-treemap-sub');if(ts)ts.textContent=crmOnbTt('treemapSub');" +
        "var h1=document.getElementById('onb-tm-h-ac');if(h1)h1.textContent=crmOnbTt('treemapAc');" +
        "var h2=document.getElementById('onb-tm-h-reg');if(h2)h2.textContent=crmOnbTt('treemapReg');" +
        "var h3=document.getElementById('onb-tm-h-ind');if(h3)h3.textContent=crmOnbTt('treemapInd');" +
        "var df=document.getElementById('onb-tm-disclaimer');if(df)df.textContent=crmOnbTt('treemapDisclaimer');" +
        "var pr=document.getElementById('parseCheckRisk');if(pr)pr.textContent=crmOnbTt('parseCheckPrefs');" +
      "}" +
      "function crmAgg(rows,keyFn){" +
        "var m={};rows.forEach(function(r){var k=keyFn(r);if(!k)return;m[k]=(m[k]||0)+r.w;});" +
        "return Object.keys(m).map(function(k){return{name:k,value:Math.round(m[k]*10)/10};})" +
        ".filter(function(x){return x.value>0;}).sort(function(a,b){return b.value-a.value;});" +
      "}" +
      "function crmTreemapOption(seriesData){" +
        "var isLight=document.documentElement.getAttribute('data-theme')==='light';" +
        "var labelColor=isLight?'#0f172a':'#f8fafc';" +
        "var border=isLight?'rgba(15,23,42,.1)':'rgba(255,255,255,.1)';" +
        "var colors=['#5b6cfb','#22c55e','#fbbf24','#fb7185','#2dd4bf','#a855f7','#f97316','#38bdf8','#f43f5e','#84cc16','#eab308'];" +
        "return{tooltip:{trigger:'item',formatter:function(p){return p.name+'<br/><b>'+p.value+'%</b>';}},animationDuration:420,animationDurationUpdate:560," +
        "series:[{type:'treemap',width:'100%',height:'100%',left:0,right:0,top:0,bottom:0,roam:false,nodeClick:false,breadcrumb:{show:false}," +
        "label:{show:true,color:labelColor,fontWeight:600,fontSize:11,overflow:'truncate',ellipsis:'…'}," +
        "upperLabel:{show:false},itemStyle:{borderColor:border,borderWidth:2,gapWidth:2,borderRadius:8}," +
        "levels:[{itemStyle:{borderWidth:0,gapWidth:3}}]," +
        "data:seriesData.map(function(d,i){return{name:d.name,value:d.value,itemStyle:{color:colors[i%colors.length]}};})}]};" +
      "}" +
      "var __crmTmCharts=[null,null,null];" +
      "function crmDisposeTreemaps(){__crmTmCharts.forEach(function(c,i){if(c){try{c.dispose();}catch(e){}__crmTmCharts[i]=null;}});}" +
      "function crmResizeTreemaps(){__crmTmCharts.forEach(function(c){try{if(c)c.resize();}catch(e){}});}" +
      "function renderAllocTreemaps(p){" +
        "if(typeof echarts==='undefined')return;" +
        "var pKey=currentPlanProfileKey||'moderate';" +
        "var rows=FUNDS.filter(function(f){return f.cat===selectedInstrumentCategory;}).map(function(f){" +
          "return{w:Number(f.pct[pKey]||0)||0,tmAc:f.tmAc,tmReg:f.tmReg,tmInd:f.tmInd};" +
        "});" +
        "var sum=rows.reduce(function(a,b){return a+b.w;},0);if(sum<=0)return;" +
        "rows=rows.map(function(r){return{w:r.w/sum*100,tmAc:r.tmAc,tmReg:r.tmReg,tmInd:r.tmInd};});" +
        "var a1=crmAgg(rows,function(r){return crmTmLabel('ac',r.tmAc);});" +
        "var a2=crmAgg(rows,function(r){return crmTmLabel('reg',r.tmReg);});" +
        "var a3=crmAgg(rows,function(r){return crmTmLabel('ind',r.tmInd);});" +
        "crmDisposeTreemaps();" +
        "function paint(id,idx,data){var el=document.getElementById(id);if(!el)return;var inst=echarts.init(el,null,{renderer:'svg'});__crmTmCharts[idx]=inst;inst.setOption(crmTreemapOption(data),true);}" +
        "paint('onb-tm-ac',0,a1);paint('onb-tm-reg',1,a2);paint('onb-tm-ind',2,a3);" +
      "}" +
      "function crmInitOnboardingUi(){" +
        "var w=document.getElementById('onb-wealth-wrap');if(!w||w.getAttribute('data-crm-bound')==='1')return;w.setAttribute('data-crm-bound','1');" +
        "w.querySelectorAll('.onb-wealth-chip').forEach(function(chip){" +
          "chip.addEventListener('click',function(){" +
            "this.classList.toggle('selected');var warn=document.getElementById('onb-wealth-warn');if(warn)warn.classList.remove('visible');" +
          "});" +
        "});" +
        "document.querySelectorAll('.onb-asset-chip').forEach(function(chip){" +
          "chip.addEventListener('click',function(){this.classList.toggle('selected');});" +
        "});" +
      "}" +
      "function crmPickDemoPrefs(variant){" +
        "document.querySelectorAll('.onb-wealth-chip').forEach(function(c){c.classList.remove('selected');});" +
        "var picks=variant==='client2'?['preserve','education','parents']:['retirement','preserve','grow','property'];" +
        "picks.forEach(function(id){var el=document.querySelector('.onb-wealth-chip[data-goal=\"'+id+'\"]');if(el)el.classList.add('selected');});" +
        "document.querySelectorAll('.onb-asset-chip').forEach(function(c){c.classList.remove('selected');});" +
        "var ap=variant==='client2'?['cash','fixed']:['equity','fixed','re'];ap.forEach(function(id){" +
          "var el=document.querySelector('.onb-asset-chip[data-asset=\"'+id+'\"]');if(el)el.classList.add('selected');" +
        "});" +
      "}" +
      "const INSTRUMENT_CATEGORIES=['Growth','Income','Stabilization','Protection'];"
    );

    h = h.replace(
      "        <!-- \\u5df2\\u6539\\u4e3a\\u53f3\\u4fa7\\u5f55\\u97f3\\u89e3\\u6790\\u64cd\\u4f5c\\u6d41\\uff0c\\u5de6\\u4fa7\\u4e0d\\u518d\\u653e AI Conversation \\u89e3\\u6790\\u6309\\u94ae -->\\n        <div class=\\\"field-grid\\\">",
      "        <!-- \\u5df2\\u6539\\u4e3a\\u53f3\\u4fa7\\u5f55\\u97f3\\u89e3\\u6790\\u64cd\\u4f5c\\u6d41\\uff0c\\u5de6\\u4fa7\\u4e0d\\u518d\\u653e AI Conversation \\u89e3\\u6790\\u6309\\u94ae -->" +
      "        <div class=\\\"onb-wealth-wrap\\\" id=\\\"onb-wealth-wrap\\\">" +
      "          <div class=\\\"onb-wealth-head\\\">" +
      "            <div class=\\\"onb-wealth-titles\\\">" +
      "              <div class=\\\"onb-kicker\\\" id=\\\"onb-wealth-kicker\\\"></div>" +
      "              <div class=\\\"onb-title\\\" id=\\\"onb-wealth-title\\\"></div>" +
      "              <div class=\\\"onb-hint\\\" id=\\\"onb-wealth-hint\\\"></div>" +
      "              <div class=\\\"onb-warn\\\" id=\\\"onb-wealth-warn\\\" role=\\\"alert\\\"></div>" +
      "            </div>" +
      "            <svg class=\\\"onb-wealth-deco\\\" viewBox=\\\"0 0 64 64\\\" aria-hidden=\\\"true\\\">" +
      "              <defs><linearGradient id=\\\"og\\\" x1=\\\"0\\\" y1=\\\"0\\\" x2=\\\"1\\\" y2=\\\"1\\\"><stop offset=\\\"0%\\\" stop-color=\\\"#FF4E50\\\"/><stop offset=\\\"100%\\\" stop-color=\\\"#9D00FF\\\"/></linearGradient></defs>" +
      "              <circle cx=\\\"32\\\" cy=\\\"32\\\" r=\\\"28\\\" fill=\\\"none\\\" stroke=\\\"url(#og)\\\" stroke-width=\\\"3\\\" opacity=\\\".35\\\"/>" +
      "              <path d=\\\"M12 40c8-14 18-18 40-16\\\" fill=\\\"none\\\" stroke=\\\"url(#og)\\\" stroke-width=\\\"3.2\\\" stroke-linecap=\\\"round\\\"/>" +
      "              <circle cx=\\\"44\\\" cy=\\\"22\\\" r=\\\"5\\\" fill=\\\"#22c55e\\\" opacity=\\\".9\\\"/>" +
      "              <rect x=\\\"14\\\" y=\\\"24\\\" width=\\\"16\\\" height=\\\"10\\\" rx=\\\"3\\\" fill=\\\"#60a5fa\\\" opacity=\\\".85\\\"/>" +
      "            </svg>" +
      "          </div>" +
      "          <div class=\\\"onb-wealth-grid\\\">" +
      "            <button type=\\\"button\\\" class=\\\"onb-wealth-chip\\\" data-goal=\\\"property\\\"><span class=\\\"onb-ico\\\"><svg viewBox=\\\"0 0 24 24\\\" fill=\\\"none\\\" stroke=\\\"#60a5fa\\\" stroke-width=\\\"1.8\\\"><path d=\\\"M4 10l8-6 8 6v10a1 1 0 01-1 1h-4v-7H9v7H5a1 1 0 01-1-1V10z\\\"/></svg></span><span class=\\\"onb-lbl\\\"></span><span class=\\\"onb-sub\\\"></span></button>" +
      "            <button type=\\\"button\\\" class=\\\"onb-wealth-chip\\\" data-goal=\\\"retirement\\\"><span class=\\\"onb-ico\\\"><svg viewBox=\\\"0 0 24 24\\\" fill=\\\"none\\\" stroke=\\\"#a855f7\\\" stroke-width=\\\"1.8\\\"><circle cx=\\\"12\\\" cy=\\\"12\\\" r=\\\"9\\\"/><path d=\\\"M12 7v6l4 2\\\"/></svg></span><span class=\\\"onb-lbl\\\"></span><span class=\\\"onb-sub\\\"></span></button>" +
      "            <button type=\\\"button\\\" class=\\\"onb-wealth-chip\\\" data-goal=\\\"education\\\"><span class=\\\"onb-ico\\\"><svg viewBox=\\\"0 0 24 24\\\" fill=\\\"none\\\" stroke=\\\"#fbbf24\\\" stroke-width=\\\"1.8\\\"><path d=\\\"M4 6h16v12H4zM8 18v4h8v-4\\\"/></svg></span><span class=\\\"onb-lbl\\\"></span><span class=\\\"onb-sub\\\"></span></button>" +
      "            <button type=\\\"button\\\" class=\\\"onb-wealth-chip\\\" data-goal=\\\"preserve\\\"><span class=\\\"onb-ico\\\"><svg viewBox=\\\"0 0 24 24\\\" fill=\\\"none\\\" stroke=\\\"#34d399\\\" stroke-width=\\\"1.8\\\"><path d=\\\"M12 3l8 4v6c0 5-3.5 9-8 10-4.5-1-8-5-8-10V7l8-4z\\\"/></svg></span><span class=\\\"onb-lbl\\\"></span><span class=\\\"onb-sub\\\"></span></button>" +
      "            <button type=\\\"button\\\" class=\\\"onb-wealth-chip\\\" data-goal=\\\"grow\\\"><span class=\\\"onb-ico\\\"><svg viewBox=\\\"0 0 24 24\\\" fill=\\\"none\\\" stroke=\\\"#f97316\\\" stroke-width=\\\"1.8\\\"><path d=\\\"M4 16l4-4 4 4 8-8\\\"/></svg></span><span class=\\\"onb-lbl\\\"></span><span class=\\\"onb-sub\\\"></span></button>" +
      "            <button type=\\\"button\\\" class=\\\"onb-wealth-chip\\\" data-goal=\\\"parents\\\"><span class=\\\"onb-ico\\\"><svg viewBox=\\\"0 0 24 24\\\" fill=\\\"none\\\" stroke=\\\"#fb7185\\\" stroke-width=\\\"1.8\\\"><circle cx=\\\"9\\\" cy=\\\"9\\\" r=\\\"3\\\"/><circle cx=\\\"17\\\" cy=\\\"9\\\" r=\\\"3\\\"/><path d=\\\"M4 20c1.5-4 5-6 8-6s6.5 2 8 6\\\"/></svg></span><span class=\\\"onb-lbl\\\"></span><span class=\\\"onb-sub\\\"></span></button>" +
      "          </div>" +
      "        </div>" +
      "        <div class=\\\"field-grid\\\">"
    );

    h = h.replace(
      "      <div class=\\\"step-panel\\\" id=\\\"step-1\\\">\\n        <div class=\\\"step-head\\\">\\n          <div class=\\\"step-head-text\\\">\\n            <div class=\\\"step-title\\\">Your Style</div>\\n            <div class=\\\"step-subtitle\\\">Select the profile that best matches the client's investor DNA.</div>\\n          </div>\\n          <div class=\\\"step-head-actions\\\" id=\\\"step-1-actions\\\"></div>\\n        </div>\\n        <div class=\\\"profile-cards\\\">",
      "      <div class=\\\"step-panel\\\" id=\\\"step-1\\\">\\n        <div class=\\\"step-head\\\">\\n          <div class=\\\"step-head-text\\\">\\n            <div class=\\\"step-title\\\">Your Style</div>\\n            <div class=\\\"step-subtitle\\\">Select the profile that best matches the client's investor DNA.</div>\\n          </div>\\n          <div class=\\\"step-head-actions\\\" id=\\\"step-1-actions\\\"></div>\\n        </div>\\n        <div class=\\\"onb-asset-wrap\\\" id=\\\"onb-asset-wrap\\\">\\n          <div class=\\\"onb-asset-head\\\">\\n            <div class=\\\"onb-kicker\\\" id=\\\"onb-asset-kicker\\\"></div>\\n            <div class=\\\"onb-title\\\" id=\\\"onb-asset-title\\\"></div>\\n            <div class=\\\"onb-hint\\\" id=\\\"onb-asset-hint\\\"></div>\\n          </div>\\n          <div class=\\\"onb-asset-grid\\\">\\n            <button type=\\\"button\\\" class=\\\"onb-asset-chip\\\" data-asset=\\\"cash\\\"><svg viewBox=\\\"0 0 48 48\\\" aria-hidden=\\\"true\\\"><rect x=\\\"8\\\" y=\\\"16\\\" width=\\\"32\\\" height=\\\"22\\\" rx=\\\"4\\\" fill=\\\"none\\\" stroke=\\\"#34d399\\\" stroke-width=\\\"2.2\\\"/><path d=\\\"M14 22h20M14 28h12\\\" stroke=\\\"#34d399\\\" stroke-width=\\\"2\\\" stroke-linecap=\\\"round\\\"/></svg><span class=\\\"onb-lbl\\\"></span><span class=\\\"onb-sub\\\"></span></button>\\n            <button type=\\\"button\\\" class=\\\"onb-asset-chip\\\" data-asset=\\\"equity\\\"><svg viewBox=\\\"0 0 48 48\\\" aria-hidden=\\\"true\\\"><path d=\\\"M8 34 L16 22 24 28 40 10\\\" fill=\\\"none\\\" stroke=\\\"#60a5fa\\\" stroke-width=\\\"2.6\\\" stroke-linecap=\\\"round\\\" stroke-linejoin=\\\"round\\\"/><circle cx=\\\"40\\\" cy=\\\"10\\\" r=\\\"3.5\\\" fill=\\\"#60a5fa\\\"/></svg><span class=\\\"onb-lbl\\\"></span><span class=\\\"onb-sub\\\"></span></button>\\n            <button type=\\\"button\\\" class=\\\"onb-asset-chip\\\" data-asset=\\\"fixed\\\"><svg viewBox=\\\"0 0 48 48\\\" aria-hidden=\\\"true\\\"><rect x=\\\"10\\\" y=\\\"14\\\" width=\\\"28\\\" height=\\\"22\\\" rx=\\\"3\\\" fill=\\\"none\\\" stroke=\\\"#fbbf24\\\" stroke-width=\\\"2.2\\\"/><path d=\\\"M14 22h20M14 30h16\\\" stroke=\\\"#fbbf24\\\" stroke-width=\\\"2\\\" stroke-linecap=\\\"round\\\"/></svg><span class=\\\"onb-lbl\\\"></span><span class=\\\"onb-sub\\\"></span></button>\\n            <button type=\\\"button\\\" class=\\\"onb-asset-chip\\\" data-asset=\\\"re\\\"><svg viewBox=\\\"0 0 48 48\\\" aria-hidden=\\\"true\\\"><path d=\\\"M10 38V18l14-8 14 8v20\\\" fill=\\\"none\\\" stroke=\\\"#a855f7\\\" stroke-width=\\\"2.2\\\" stroke-linejoin=\\\"round\\\"/><path d=\\\"M18 38V26h12v12\\\" fill=\\\"none\\\" stroke=\\\"#a855f7\\\" stroke-width=\\\"2\\\"/></svg><span class=\\\"onb-lbl\\\"></span><span class=\\\"onb-sub\\\"></span></button>\\n          </div>\\n        </div>\\n        <div class=\\\"profile-cards\\\">"
    );

    h = h.replace(
      "          </div>\\n          </div>\\n          <!-- \\u4e1a\\u52a1\\u8bf4\\u660e\\uff1aGrowth \\u4e0e AI \\u6458\\u8981\\u4e0a\\u4e0b\\u6392\\u5217\\uff0c\\u52a0\\u5bbd\\u5bb9\\u5668\\u5185\\u81ea\\u9002\\u5e94\\u56fe\\u8868\\u4e0e\\u6587\\u6848 -->\\n          <div class=\\\"plan-timeline-ai-stack\\\">",
      "          </div>\\n          </div>\\n          <div class=\\\"onb-treemap-wrap\\\" id=\\\"onb-treemap-wrap\\\">\\n            <div class=\\\"onb-treemap-head\\\">\\n              <div class=\\\"onb-title\\\" id=\\\"onb-treemap-title\\\"></div>\\n              <div class=\\\"onb-sub\\\" id=\\\"onb-treemap-sub\\\"></div>\\n            </div>\\n            <div class=\\\"onb-treemap-grid\\\">\\n              <div class=\\\"onb-tm-card\\\"><div class=\\\"onb-tm-hd\\\" id=\\\"onb-tm-h-ac\\\"></div><div class=\\\"onb-tm-chart\\\" id=\\\"onb-tm-ac\\\"></div></div>\\n              <div class=\\\"onb-tm-card\\\"><div class=\\\"onb-tm-hd\\\" id=\\\"onb-tm-h-reg\\\"></div><div class=\\\"onb-tm-chart\\\" id=\\\"onb-tm-reg\\\"></div></div>\\n              <div class=\\\"onb-tm-card\\\"><div class=\\\"onb-tm-hd\\\" id=\\\"onb-tm-h-ind\\\"></div><div class=\\\"onb-tm-chart\\\" id=\\\"onb-tm-ind\\\"></div></div>\\n            </div>\\n            <div class=\\\"onb-tm-foot\\\" id=\\\"onb-tm-disclaimer\\\"></div>\\n          </div>\\n          <!-- \\u4e1a\\u52a1\\u8bf4\\u660e\\uff1aGrowth \\u4e0e AI \\u6458\\u8981\\u4e0a\\u4e0b\\u6392\\u5217\\uff0c\\u52a0\\u5bbd\\u5bb9\\u5668\\u5185\\u81ea\\u9002\\u5e94\\u56fe\\u8868\\u4e0e\\u6587\\u6848 -->\\n          <div class=\\\"plan-timeline-ai-stack\\\">"
    );

    h = h.replace(
      "function nextStep(){if(currentStep<2){currentStep++;render()}}",
      "function nextStep(){if(currentStep===0){var n=document.querySelectorAll('.onb-wealth-chip.selected').length;if(!n){var warn=document.getElementById('onb-wealth-warn');if(warn)warn.classList.add('visible');return;}}if(currentStep<2){currentStep++;render()}}"
    );

    h = h.replace(
      "renderDonut(p);",
      "renderDonut(p);if(typeof renderAllocTreemaps==='function'){try{renderAllocTreemaps(p);}catch(e){}}"
    );

    h = h.replace(
      "  const btnCxl=document.getElementById('btn-cancel-recording-import'); if(btnCxl) btnCxl.textContent=tt('cancel');\\n}",
      "  const btnCxl=document.getElementById('btn-cancel-recording-import'); if(btnCxl) btnCxl.textContent=tt('cancel');\\n  if(typeof crmRefreshOnbDom==='function') crmRefreshOnbDom();\\n}"
    );

    h = h.replace(
      "window.addEventListener('resize',()=>{\\n  setTimeout(notifyParentHeight,60);\\n  if(typeof timelineChart!=='undefined'&&timelineChart) try{timelineChart.resize();}catch(e){}\\n});",
      "window.addEventListener('resize',()=>{\\n  setTimeout(notifyParentHeight,60);\\n  if(typeof timelineChart!=='undefined'&&timelineChart) try{timelineChart.resize();}catch(e){}\\n  if(typeof crmResizeTreemaps==='function') try{crmResizeTreemaps();}catch(e){}\\n});"
    );

    h = h.replace(
      "applyLocale(currentLocale);",
      "crmInitOnboardingUi();applyLocale(currentLocale);if(typeof crmRefreshOnbDom==='function')crmRefreshOnbDom();"
    );

    h = h.replace(
      "progressLabels:['About You','Your Style','Your Plan']",
      "progressLabels:['About You','Preferences','Your Plan']"
    );
    h = h.replace("step2Title:'Your Style'", "step2Title:'Preferences'");
    h = h.replace(
      "progressLabels:['基本信息','风险偏好','配置方案']",
      "progressLabels:['基本信息','客户偏好','配置方案']"
    );
    h = h.replace("step2Title:'风险偏好'", "step2Title:'客户偏好'");
    h = h.replace(
      "progressLabels:['基本資料','風險偏好','配置方案']",
      "progressLabels:['基本資料','客戶偏好','配置方案']"
    );
    h = h.replace("step2Title:'風險偏好'", "step2Title:'客戶偏好'");
    h = h.replace(
      "progressLabels:['お客様情報','投資スタイル','提案プラン']",
      "progressLabels:['お客様情報','嗜好設定','提案プラン']"
    );
    h = h.replace("step2Title:'投資スタイル'", "step2Title:'嗜好設定'");

    return h;
  }
'''.strip("\n")


def main():
    text = PATH.read_text(encoding="utf-8", errors="replace")
    anchor = "function mountEmbeddedAllocationIframes() {\n  function normalizeEmbeddedAllocationHtml(html) {"
    if "function applyCrmOnboardingEnhancements(html)" in text:
        print("Already injected; skip")
        return
    if anchor not in text:
        raise SystemExit("anchor not found")
    text = text.replace(anchor, "function mountEmbeddedAllocationIframes() {\n" + APPLY_FN + "\n  function normalizeEmbeddedAllocationHtml(html) {", 1)

    ret = "    );\n    return next;\n  }\n  function getEmbeddedAllocationHtml()"
    if "applyCrmOnboardingEnhancements" not in text.split("return next;")[0].split("function normalizeEmbeddedAllocationHtml")[-1]:
        text = text.replace(
            ret,
            "    );\n    if (next.indexOf(\"CRM onboarding wealth goals v1\") === -1) {\n      next = applyCrmOnboardingEnhancements(next);\n    }\n    return next;\n  }\n  function getEmbeddedAllocationHtml()",
            1,
        )

    risk_line = '      "  if(checkedSet.includes(\'risk\')){\\n" +\n      "    selectedProfile=data.profile||\'moderate\';\\n" +'
    risk_new = (
        '      "  if(checkedSet.includes(\'risk\')){\\n" +\n'
        '      "    try{if(typeof crmPickDemoPrefs===\\\'function\\\')crmPickDemoPrefs(variant);}catch(e){}\\n" +\n'
        '      "    selectedProfile=data.profile||\'moderate\';\\n" +'
    )
    if risk_new.strip() not in text and risk_line in text:
        text = text.replace(risk_line, risk_new, 1)

    PATH.write_text(text, encoding="utf-8")
    print("OK: patched", PATH)


if __name__ == "__main__":
    main()
