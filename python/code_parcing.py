import re
import pandas as pd

input_text = """
{name: 'Dana Benyehuda', email: 'bydana@theagencyre.com', phone: '(323) 304-2076 License: DRE #01993117'}
196
: 
{name: 'Dana Christensen', email: 'dana.christensen@theagencyre.com', phone: '(949) 315-9720 License: DRE #01920317'}
197
: 
{name: 'Dana Weiler', email: 'dana.weiler@theagencyre.com', phone: '(925) 998-8470 License: DRE #956555'}
198
: 
{name: "Dani O'Connell", email: 'dani.oconnell@theagencyre.com', phone: '(925) 786-2176 License: DRE # 01892167'}
199
: 
{name: 'Daniel Clark', email: 'dan.clark@theagencyre.com', phone: '(415) 317-0286 License: DRE #01429807'}
200
: 
{name: 'Daniel Lam', email: 'dlam@theagencyre.com', phone: '(213) 926-3375 License: DRE #1510101'}
201
: 
{name: 'Daniel Levin', email: 'daniel.levin@theagencyre.com', phone: '(310) 579-5071 License: DRE #1994876'}
202
: 
{name: 'Daniel Ohana', email: 'daniel.ohana@theagencyre.com', phone: '(818) 633-5521 License: DRE #01941646'}
203
: 
{name: 'Daniel Shalvardzhyan', email: 'daniel.s@theagencyre.com', phone: '(818) 939-1439 License: DRE #01937402'}
204
: 
{name: 'Daniel Stevenson', email: 'dstevenson@theagencyre.com', phone: '(424) 271-3344 License: DRE #1981172'}
205
: 
{name: 'Danielle Lockwood', email: 'danielle.l@theagencyre.com', phone: '(310) 497-5771 License: DRE #02009408'}
206
: 
{name: 'Danielle Yeretzian', email: 'danielle.yeretzian@theagencyre.com', phone: '(310) 871-1538 License: DRE #02035013'}
207
: 
{name: 'Danny Cerecedes', email: 'danny.cerecedes@theagencyre.com', phone: '(818) 660-6752 License: DRE #1865922'}
208
: 
{name: 'Darian Robin', email: 'drobin@theagencyre.com', phone: '(310) 963-9471 License: DRE #1410426'}
209
: 
{name: 'David Findley', email: 'david.findley@theagencyre.com', phone: '(310) 345-6911 License: DRE #641180'}
210
: 
{name: 'David Melaugh', email: 'dmelaugh@theagencyre.com', phone: '(310) 422-1561 License: DRE #1862538'}
211
: 
{name: 'David Ontiveros', email: 'david.ontiveros@theagencyre.com', phone: '(650) 492-1157 License: DRE #02115155'}
212
: 
{name: 'David Parnes', email: 'dparnes@theagencyre.com', phone: '(424) 400-5916 License: DRE #01905862'}
213
: 
{name: 'Dea Campbell', email: 'dea.campbell@theagencyre.com', phone: '(925) 640-1727 License: DRE #1734129'}
214
: 
{name: 'Deb Klein', email: 'deb.klein@theagencyre.com', phone: '(760) 803-6796 License: DRE #01958711'}
215
: 
{name: 'Debra Jaffe', email: 'djaffe@theagencyre.com', phone: '(424) 230-7433 License: DRE #01921806'}
216
: 
{name: 'Deedee Howard', email: 'dhoward@theagencyre.com', phone: '(424) 230-3755 License: DRE #1039224'}
217
: 
{name: 'DeeDee Cortese', email: 'deedee.cortese@theagencyre.com', phone: '(310) 200-8262 License: DRE #01887457'}
218
: 
{name: 'Deneka Waddell', email: 'deneka.w@theagencyre.com', phone: '(949) 607-7143 License: DRE #02121480'}
219
: 
{name: 'Denise Snanoudj', email: 'denise.s@theagencyre.com', phone: '(818) 924-2655 License: DRE #1101684'}
220
: 
{name: 'Dennis Chernov', email: 'dennis@theagencyre.com', phone: '(818) 355-2461 License: DRE #1850113'}
221
: 
{name: 'Dian McManus', email: 'dianmcmanus@theagencyre.com', phone: '(310) 980-7034 License: DRE #02080334'}
222
: 
{name: 'Diane Chesler', email: 'diane.chesler@theagencyre.com', phone: '(650) 888-7899 License: DRE #00675583'}
223
: 
{name: 'Dominique Cristall', email: 'dominique.cristall@theagencyre.com', phone: '(310) 717-3026 License: DRE #02168580'}
224
: 
{name: 'Doug Carver', email: 'doug.carver@theagencyre.com', phone: '(626) 524-2712 License: DRE #01892409'}
225
: 
{name: 'Drew Carlson', email: 'drew.carlson@theagencyre.com', phone: '(612) 701-2090 License: DRE #02138797'}
226
: 
{name: 'Drew Jacobson', email: 'drew.jacobson@theagencyre.com', phone: '(310) 486-1697 License: DRE #01831497'}
227
: 
{name: 'Eduardo Umansky', email: 'eumansky@theagencyre.com', phone: '(310) 490-4331 License: DRE #1354521'}
228
: 
{name: 'Edward Fitz', email: 'efitz@theagencyre.com', phone: '(310) 650-0052 License: DRE #1023092'}
229
: 
{name: 'Elaine Klemm', email: 'elaine.klemm@theagencyre.com', phone: '(650) 269-1035 License: DRE #00972243'}
230
: 
{name: 'Eldon Daetweiler', email: 'eldon.daetweiler@theagencyre.com', phone: '(310) 946-9349 License: DRE #1311184'}
231
: 
{name: 'Elham Shaoulian', email: 'elham.s@theagencyre.com', phone: '(310) 228-0109 License: DRE #02003789'}
232
: 
{name: 'Elina Shidaeva', email: 'elina.s@theagencyre.com', phone: '(310) 919-0011 License: DRE #02077294'}
233
: 
{name: 'Elise Travis', email: 'elle.travis@theagencyre.com', phone: '(714) 932-3105 License: DRE #2017434'}
234
: 
{name: 'Elise Vives', email: 'Krueger', phone: 'elise.viveskrueger@theagencyre.com (510) 829-6093 License: DRE # 02127421'}
235
: 
{name: 'Elizabeth Thompson', email: 'elizabeth.thompson@theagencyre.com', phone: '(650) 823-8904 License: DRE #01382997'}
236
: 
{name: 'Ellie Hartoonian', email: 'ellie@theagencyre.com', phone: '(818) 262-2202 License: DRE #1944092'}
237
: 
{name: 'Elli Hope', email: 'Pendley', phone: 'elli.hope.pendley@theagencyre.com (925) 557-5655 License: DRE #1867534'}
238
: 
{name: 'Ellis Clark', email: 'ellis.clark@theagencyre.com', phone: '(510) 393-8147 License: DRE #01954136'}
239
: 
{name: 'Emil Hartoonian', email: 'ehartoonian@theagencyre.com', phone: '(310) 990-0063 License: DRE #01796925'}
240
: 
{name: 'Emilee Sutherland', email: 'emilee.sutherland@theagencyre.com', phone: '(951) 870-9008 License: DRE #02166140'}
241
: 
{name: 'Emily Fang', email: 'emily.fang@theagencyre.com', phone: '(650) 275-3098 License: DRE #01854906'}
242
: 
{name: 'Emma Korchek', email: 'emma.korchek@theagencyre.com', phone: '(818) 300-5027 License: DRE #02013676'}
243
: 
{name: 'Eric Haskell', email: 'eric.haskell@theagencyre.com', phone: '(805) 570-7243 License: DRE #1866805'}
244
: 
{name: 'Erica Rivas', email: 'erivas@theagencyre.com', phone: '(818) 257-1054 License: DRE #1788685'}
245
: 
{name: 'Erin Carrigg', email: 'erin.carrigg@theagencyre.com', phone: '(925) 360-4420 License: DRE #02020465'}
246
: 
{name: 'Esther "Evie"', email: 'Silvas', phone: 'evie.silvas@theagencyre.com (323) 404-5293'}
247
: 
{name: 'Ethan Applen', email: 'ethan.applen@theagencyre.com', phone: '(818) 522-4827 License: DRE #02136266'}
248
: 
{name: 'Eva Ustupski', email: 'eva.ustupski@theagencyre.com', phone: '(949) 607-6120 License: DRE #02140562'}
249
: 
{name: 'Evan Ferrante', email: 'evan.ferrante@theagencyre.com', phone: '(914) 720-8134 License: DRE #2151154'}
250
: 
{name: 'Evan Zurn', email: 'evan.zurn@theagencyre.com', phone: '(760) 793-6356 License: DRE #01957746'}
251
: 
{name: 'Eytan Levin', email: 'eytan.levin@theagencyre.com', phone: '(310) 924-0806 License: DRE #01324953'}
252
: 
{name: 'Farah Levi', email: 'farah.levi@theagencyre.com', phone: '(310) 978-7555 License: DRE #01825849'}
253
: 
{name: 'Farrah Brittany', email: 'farrah@theagencyre.com', phone: '(424) 230-3712 License: DRE #1933070'}
254
: 
{name: 'Feroz Taj', email: 'feroz@theagencyre.com', phone: '(310) 614-5893 License: DRE #02004840'}
255
: 
{name: 'Fred Dapp', email: 'fred.dapp@theagencyre.com', phone: '(310) 728-0533 License: DRE #02048450'}
256
: 
{name: 'Fred Fallah', email: 'fred.fallah@theagencyre.com', phone: '(650) 888-2612 License: DRE #01457716'}
257
: 
{name: 'Freddy Thomas', email: 'freddy.thomas@theagencyre.com', phone: '(310) 990-8892 License: DRE #2107890'}
258
: 
{name: 'Gary Herbert', email: 'gary.herbert@theagencyre.com', phone: '(650) 799-4021 License: DRE #00762521'}
259
: 
{name: 'Gary Hill', email: 'gary.hill@theagencyre.com', phone: '(408) 309-3565 License: DRE #00783952'}
260
: 
{name: 'Gaston Bustamante', email: 'gaston.bustamante@theagencyre.com', phone: '(619) 279-7103 License: DRE #01990465'}
261
: 
{name: 'Genella Williamson', email: 'genella.w@theagencyre.com', phone: '(650) 787-0839 License: DRE #00755754'}
262
: 
{name: 'George Ouzounian', email: 'george.oz@theagencyre.com', phone: '(818) 900-4259 License: DRE #01948763'}
263
: 
{name: 'Gerry Geoghegan', email: 'gerardg@theagencyre.com', phone: '(408) 896-5626 License: DRE #01895141'}
264
: 
{name: 'Gideon Lang-Laddie', email: 'gideon@theagencyre.com', phone: '(424) 222-8112 License: DRE #2041370'}
265
: 
{name: 'Gillian Jones', email: 'gillian.jones@theagencyre.com', phone: '(760) 485-7546 License: DRE #1404006'}
266
: 
{name: 'Gina Martino', email: 'gmartino@theagencyre.com', phone: '(424) 230-3759 License: DRE #1042370'}
267
: 
{name: 'Gina Michelle', email: 'gina.michelle@theagencyre.com', phone: '(818) 850-1458 License: DRE #01503003'}
268
: 
{name: 'Gioia Black', email: 'gioia.black@theagencyre.com', phone: '(619) 414-9851 License: DRE # 02139684'}
269
: 
{name: 'Glenna R.', email: 'Castrillo', phone: 'glenna@theagencyre.com (310) 346-1949 License: DRE #01966498'}
270
: 
{name: 'Gloria Castellanos', email: 'gcastellanos@theagencyre.com', phone: '(424) 400-5969 License: DRE #01449423'}
271
: 
{name: 'Grant Law', email: 'glaw@theagencyre.com', phone: '(626) 888-1540 License: DRE #01757046'}
272
: 
{name: 'Greg Jackson', email: 'greg.jackson@theagencyre.com', phone: '(925) 786-8504 License: DRE #01111634'}
273
: 
{name: 'Greg Miller', email: 'greg.miller@theagencyre.com', phone: '(818) 527-2246 License: DRE #01958031'}
274
: 
{name: 'Greg Schoch', email: 'greg.schoch@theagencyre.com', phone: '(310) 463-0343 License: DRE #01864655'}
275
: 
{name: 'Greg Shenon', email: 'greg.shenon@theagencyre.com', phone: '(818) 642-2861 License: DRE #2039595'}
276
: 
{name: 'Greg Stangl', email: 'greg.stangl@theagencyre.com', phone: '(213) 327-5436 License: DRE #1440433'}
277
: 
{name: 'Gregory Mayo', email: 'g.mayo@theagencyre.com', phone: '(408) 438-3180 License: DRE #01964504'}
278
: 
{name: 'Griffin Riddle', email: 'griffin.riddle@theagencyre.com', phone: '(424) 320-9348 License: DRE #1949069'}
279
: 
{name: 'Griffin Sweet', email: 'griffin.sweet@theagencyre.com', phone: '(310) 339-1171 License: DRE #2078712'}
280
: 
{name: 'Grigor Aleksanian', email: 'grigor.alek@theagencyre.com', phone: '(818) 667-7641 License: DRE #2069401'}
281
: 
{name: 'Gus Ruelas', email: 'gus@theagencyre.com', phone: '(626) 375-5401 License: DRE #1221146'}
282
: 
{name: 'Guy Azar', email: 'guy.azar@theagencyre.com', phone: '(818) 339-4192 License: DRE #01882376'}
283
: 
{name: 'Hailey Collins', email: 'hailey.collins@theagencyre.com', phone: '(561) 213-2308 License: DRE #02130163'}
284
: 
{name: 'Hana Cha', email: 'hana@theagencyre.com', phone: '(424) 230-7809 License: DRE #1882080'}
285
: 
{name: 'Heather Bell', email: 'heather.bell@theagencyre.com', phone: '(310) 779-7211 License: DRE #1897826'}
286
: 
{name: 'Heather Boyd', email: 'hboyd@theagencyre.com', phone: '(310) 994-3140 License: DRE #01836830'}
287
: 
{name: 'Heather Daum', email: 'heather.daum@theagencyre.com', phone: '(916) 215-5390 License: DRE #01876992'}
288
: 
{name: 'Heather Wildman', email: 'heatherwildman@theagencyre.com', phone: '(310) 936-7405 License: DRE #02207723'}
289
: 
{name: 'Helene Barkin', email: 'helene.barkin@theagencyre.com', phone: '(510) 331-1122 License: DRE #01032351'}
290
: 
{name: 'Holly Hatch', email: 'holly.hatch@theagencyre.com', phone: '(818) 306-7901 License: DRE #01244574'}
291
: 
{name: 'Hovik Pakhanyan', email: 'hovik.p@theagencyre.com', phone: '(626) 660-5423 License: DRE #2047126'}
292
: 
{name: 'Ingrid Sacerio', email: 'isacerio@theagencyre.com', phone: '(424) 354-4887 License: DRE #01905431'}
293
: 
{name: 'Irene Dazzan-Palmer', email: 'irene.dazzan@theagencyre.com', phone: '(310) 418-3777 License: DRE #597226'}
294
: 
{name: 'Isaac Levy', email: 'isaac.levy@theagencyre.com', phone: '(512) 470-7595 License: DRE #02169259'}
295
: 
{name: 'Ivan Martinez', email: 'ivan.martinez@theagencyre.com', phone: '(619) 386-5363 License: DRE # 02177500'}
296
: 
{name: 'Ivan Vargas', email: 'ivan.vargas@theagencyre.com', phone: '(310) 709-2352 License: DRE #02062068'}
297
: 
{name: 'Jack Burley', email: 'jack.burley@theagencyre.com', phone: '(510) 735-5585 License: DRE #02134890'}
298
: 
{name: 'Jack Lando', email: 'jlando@theagencyre.com', phone: '(310) 663-7928 License: DRE #02197902'}
299
: 
{name: 'Jacob Weinblut', email: 'jacob.weinblut@theagencyre.com', phone: '(818) 644-7533 License: DRE #2090454'}
300
: 
{name: 'Jacqueline Kuykendall', email: 'jacqueline.k@theagencyre.com', phone: '(626) 676-9471 License: DRE #2005448'}
301
: 
{name: 'Jaime Cuevas', email: 'jaime@theagencyre.com', phone: '(310) 593-3200 License: DRE #01265409'}
302
: 
{name: 'James Harris', email: 'james@theagencyre.com', phone: '(424) 400-5915 License: DRE #1909801'}
303
: 
{name: 'James Hirsch', email: 'jhirsch@theagencyre.com', phone: '(310) 413-7414 License: DRE #1970186'}
304
: 
{name: 'Jamie Camp', email: 'jamie.camp@theagencyre.com', phone: '(818) 251-0450 License: DRE #01923825'}
305
: 
{name: 'Jamie Waryck', email: 'jamie.waryck@theagencyre.com', phone: '(310) 944-1945 License: DRE #1898871'}
306
: 
{name: 'Jana Charalambous', email: 'jana.charalambous@theagencyre.com', phone: '(310) 270-3449 License: DRE #01445651'}
307
: 
{name: 'Janet Jensen', email: 'janet@theagencyloscabos.com', phone: '+52 624 141 6726'}
308
: 
{name: 'Jared Higgins', email: 'jared.higgins@theagencyre.com', phone: '(925) 487-2907 License: DRE #1781054'}
309
: 
{name: 'Jason Bergman', email: 'j.bergman@theagencyre.com', phone: '(626) 394-0900 License: DRE #02097939'}
310
: 
{name: 'Jason Kim', email: 'jason.kim@theagencyre.com', phone: '(213) 422-3093 License: DRE #02007887'}
311
: 
{name: 'Jason Walker', email: 'jason.walker@theagencyre.com', phone: '(310) 623-0203 License: DRE #1347583'}
312
: 
{name: 'Javier Andres', email: 'Ramirez', phone: 'javier.ramirez@theagencyre.com (619) 939-9862 License: DRE #02200036'}
313
: 
{name: 'Javin Hope', email: 'javin.hope@theagencyre.com', phone: '(858) 922-2202 License: DRE #01750598'}
314
: 
{name: 'Jay Ravnikar', email: 'jay.ravnikar@theagencyre.com', phone: '(818) 961-6565 License: DRE #1992633'}
315
: 
{name: 'Jean-Baptiste Rugiero', email: 'jrugiero@theagencyre.com', phone: '(424) 335-1045 License: DRE #01913472'}
316
: 
{name: 'Jeannine Savory', email: 'jeannine.savory@theagencyre.com', phone: '(619) 800-0289 License: DRE #01310559'}
317
: 
{name: 'Jeff Atwood', email: 'jeff.atwood@theagencyre.com', phone: '(408) 313-2805 License: DRE #01120832'}
318
: 
{name: 'Jeff Barnett', email: 'jeff.barnett@theagencyre.com', phone: '(408) 460-1393 License: DRE # 01019707'}
319
: 
{name: 'Jeff Kohl', email: 'jkohl@theagencyre.com', phone: '(310) 625-9035 License: DRE #01095791'}
320
: 
{name: 'Jeff Samuels', email: 'jeff.samuels@theagencyre.com', phone: '(925) 708-0407 License: DRE #01440794'}
321
: 
{name: 'Jennie Priel', email: 'jennie.priel@theagencyre.com', phone: '(818) 231-5882 License: DRE #02065941'}
322
: 
{name: 'Jennifer Newsome', email: 'j.newsome@theagencyre.com', phone: '(818) 645-0348 License: DRE #02029551'}
323
: 
{name: 'Jennifer Perez', email: 'j.perez@theagencyre.com', phone: '(818) 299-3880 License: DRE #02125070'}
324
: 
{name: 'Jennifer Plotkin', email: 'jennifer.plotkin@theagencyre.com', phone: '(818) 470-7358 License: DRE #02036025'}
325
: 
{name: 'Jennifer Purdue', email: 'jennifer.purdue@theagencyre.com', phone: '(310) 721-3313 License: DRE #01273915'}
326
: 
{name: 'Jennifer Tisdale', email: 'jennifer.tisdale@theagencyre.com', phone: '(818) 590-5365 License: DRE #02131592'}
327
: 
{name: 'Jeremy Greenberg', email: 'jgreenberg@theagencyre.com', phone: '(415) 577-6994 License: DRE #02071906'}
328
: 
{name: 'Jeromy Robert', email: 'jeromy.robert@theagencyre.com', phone: '(310) 467-7490 License: DRE #02068461'}
329
: 
{name: 'Jessica Koltsov', email: 'jkoltsov@theagencyre.com', phone: '(310) 430-3420 License: DRE #2022522'}
330
: 
{name: 'Jessica Michalov', email: 'jessica.michalov@theagencyre.com', phone: '(310) 362-5972 License: DRE #2133516'}
331
: 
{name: 'Jessica Soo', email: 'jessica.soo@theagencyre.com', phone: '(626) 453-6567 License: DRE #02011934'}
332
: 
{name: 'Jessica Wychico', email: 'jessica.wychico@theagencyre.com', phone: '(626) 228-5684 License: DRE #02022143'}
333
: 
{name: 'Jessie Stockstad', email: 'jstockstad@theagencyre.com', phone: '(424) 249-7041 License: DRE #02084293'}
334
: 
{name: 'Jill Fusari', email: 'jill.fusari@theagencyre.com', phone: '(925) 817-7818 License: DRE #1775608'}
335
: 
{name: 'Jill Jadon', email: 'jill.jadon@theagencyre.com', phone: '(310) 968-2956 License: DRE #2137608'}
336
: 
{name: 'Jill Nelsen', email: 'jill.nelsen@theagencyre.com', phone: '(424) 221-5020 License: DRE #2050427'}
337
: 
{name: 'Jim Lowell', email: 'jim.lowell@theagencyre.com', phone: '(831) 902-0777 License: DRE #00883474'}
338
: 
{name: 'Jim Nappo', email: 'jim.nappo@theagencyre.com', phone: '(650) 906-5775 License: DRE #00767311'}
339
: 
{name: 'Jim Wright', email: 'jim.wright@theagencyre.com', phone: '(925) 998-7186 License: DRE #917625'}
340
: 
{name: 'Jimmy Kerr', email: 'jimmy.kerr@theagencyre.com', phone: '(619) 857-2294 License: DRE # 01996255'}
341
: 
{name: 'Jimmy Nappo', email: 'jimmy.nappo@theagencyre.com', phone: '(650) 861-7661 License: DRE #01439226'}
342
: 
{name: 'Joan Lamond', email: 'joan.lamond@theagencyre.com', phone: '(323) 628-6122 License: DRE #02064539'}
343
: 
{name: 'Joey Ben-Zvi', email: 'joey.bz@theagencyre.com', phone: '(424) 832-0387 License: DRE #02087083'}
344
: 
{name: 'Joey Brauer', email: 'jbrauer@theagencyre.com', phone: '(310) 499-3813 License: DRE #1949799'}
345
: 
{name: 'Joey Parsi', email: 'joey.parsi@theagencyre.com', phone: '(310) 780-0770 License: DRE #02126421'}
346
: 
{name: 'John McCann', email: 'jmccann@theagencyre.com', phone: '(424) 231-2396 License: DRE #1948109'}
347
: 
{name: 'John Tashtchian', email: 'john.t@theagencyre.com', phone: '(818) 968-2822 License: DRE #01453364'}
348
: 
{name: 'John Torres', email: 'john.torres@theagencyre.com', phone: '(707) 494-4948 License: DRE #00892520'}
349
: 
{name: 'Jon Gednalske', email: 'jon.gednalske@theagencyre.com', phone: '(605) 254-2977 License: DRE #02199008'}
350
: 
{name: 'Jon Grauman', email: 'jgrauman@theagencyre.com', phone: '(424) 600-7576 License: DRE #1469825'}
351
: 
{name: 'Jon Smith', email: 'jon.smith@theagencyre.com', phone: '(323) 309-6416 License: DRE #01959566'}
352
: 
{name: 'Jon Swire', email: 'jswire@theagencyre.com', phone: '(310) 948-2631 License: DRE #1336277'}
353
: 
{name: 'Jonathan Broberg', email: 'jbroberg@theagencyre.com', phone: '(424) 385-4446 License: DRE #02037719'}
354
: 
{name: 'Jonathan Carr', email: 'jcarr@theagencyre.com', phone: '(203) 644-2799 License: DRE #02064561'}
355
: 
{name: 'Jonathan Ruiz', email: 'jr@theagencyre.com', phone: '(424) 230-3714 License: DRE #1886713'}
356
: 
{name: 'Jordan Ginsburg', email: 'jordan.ginsburg@theagencyre.com', phone: '(818) 422-9232 License: DRE #2099575'}
357
: 
{name: 'Jordan Gonda', email: 'jordan.gonda@theagencyre.com', phone: '(310) 866-2222 License: DRE #02203289'}
358
: 
{name: 'Jordan A.', email: 'Nedeff', phone: 'jordan.a.nedeff@theagencyre.com (626) 755-9291 License: DRE #01374071'}
359
: 
{name: 'Jorge Ahuage', email: 'jorge.ahuage@theagencyre.com', phone: '(619) 504-7777 License: DRE #01124056'}
360
: 
{name: 'Jose Vidal', email: 'jose.vidal@theagencyre.com', phone: '(818) 384-8306 License: DRE #02014729'}
361
: 
{name: 'Josephine Amin', email: 'josephine.amin@theagencyre.com', phone: '(310) 407-9299 License: DRE #02062607'}
362
: 
{name: 'Josette Wolf', email: 'josette.wolf@theagencyre.com', phone: '(626) 264-0425 License: DRE #01787295'}
363
: 
{name: 'Josh Myler', email: 'jmyler@theagencyre.com', phone: '(323) 333-0301 License: DRE #1443547'}
364
: 
{name: 'Joshua Kashani', email: 'joshkashani@theagencyre.com', phone: '(310) 779-1995 License: DRE #02102256'}
365
: 
{name: 'Judy Bogard-Tanigami', email: 'judy.bogard@theagencyre.com', phone: '(650) 207-2111 License: DRE #00298975'}
366
: 
{name: 'Julia Derrick', email: 'julia.d@theagencyre.com', phone: '(323) 384-4700 License: DRE #02138214'}
367
: 
{name: 'Julie Pae', email: 'julie.pae@theagencyre.com', phone: '(408) 891-6675 License: DRE #01724555'}
368
: 
{name: 'Justin Bono', email: 'justin.bono@theagencyre.com', phone: '(714) 343-8291 License: DRE #2135999'}
369
: 
{name: 'Justin Bowen-Taylor', email: 'j.bowentaylor@theagencyre.com', phone: '(310) 350-7031 License: DRE #02030372'}
370
: 
{name: 'Justin Ceeko', email: 'justin.ceeko@theagencyre.com', phone: '(760) 218-6643 License: DRE #1928804'}
371
: 
{name: 'Kannika Kim', email: 'k.kim@theagencyre.com', phone: '(916) 833-8379 License: DRE #02136089'}
372
: 
{name: 'Karen Klein', email: 'karen.klein@theagencyre.com', phone: '(818) 324-6518 License: DRE #01349947'}
373
: 
{name: 'Karen Lowe', email: 'karenlowe@theagencyre.com', phone: '(310) 995-2622 License: DRE #02152213'}
374
: 
{name: 'Karen Mahoney', email: 'karen.mahoney@theagencyre.com', phone: '(949) 370-5400 License: DRE #1092395'}
375
: 
{name: 'Karen Morris', email: 'kmorris@theagencyre.com', phone: '(760) 269-3186 License: DRE # 01974781'}
376
: 
{name: 'Karen Richardson', email: 'karen.richardson@theagencyre.com', phone: '(647) 368-6167 License: DRE #01407557'}
377
: 
{name: 'Karen Silver', email: 'karen.silver@theagencyre.com', phone: '(310) 871-4208 License: DRE #1985126'}
378
: 
{name: 'Karine Aslanian', email: 'karine.aslanian@theagencyre.com', phone: '(818) 355-4906 License: DRE #1331967'}
379
: 
{name: 'Karlon Dawson', email: 'karlon.dawson@theagencyre.com', phone: '(818) 554-9645 License: DRE #02206353'}
380
: 
{name: 'Kate Adams', email: 'Barnett', phone: 'kate.adams@theagencyre.com (626) 660-7474 License: DRE #01310017'}
381
: 
{name: 'Kathrin Nicholson', email: 'knicholson@theagencyre.com', phone: '(424) 231-0751 License: DRE #01273016'}
382
: 
{name: 'Kathy Stauffer', email: 'kathy.stauffer@theagencyre.com', phone: '(707) 280-6257 License: DRE #01364735'}
383
: 
{name: 'Katrina Palandri', email: 'katrina.palandri@theagencyre.com', phone: '(213) 550-8184 License: DRE #2003691'}
384
: 
{name: 'Kaylin Cañada', email: 'kaylin.canada@theagencyre.com', phone: '(818) 917-4171 License: DRE #02188815'}
385
: 
{name: 'Kellianne Rapoza', email: 'kellianne.rapoza@theagencyre.com', phone: '(925) 257-4068 License: DRE #02009834'}
386
: 
{name: 'Kelly Pavlick', email: 'kelly.pavlick@theagencyre.com', phone: '(619) 913-9127 License: DRE #02013971'}
387
: 
{name: 'Ken Whelan', email: 'ken.whelan@theagencyre.com', phone: '(310) 500-6144 License: DRE #02056174'}
388
: 
{name: 'Kendra McLeish', email: 'kendra.mcleish@theagencyre.com', phone: '(619) 925-6160 License: DRE #02202806'}
389
: 
{name: 'Kendra Wilson', email: 'kwilson@theagencyre.com', phone: '(424) 400-5923 License: DRE #1930432'}
390
: 
{name: 'Kenneth Spadoni', email: 'ken.spadoni@theagencyre.com', phone: '(707) 494-9807 License: DRE #00716861'}
391
: 
{name: 'Kerry Kimble', email: 'kerry.kimble@theagencyre.com', phone: '(818) 433-1942 License: DRE #2054640'}
392
: 
{name: 'Kevin Dees', email: 'kdees@theagencyre.com', phone: '(424) 281-6848 License: DRE #1915567'}
393
: 
{name: 'Kevin Goldman', email: 'kevin.goldman@theagencyre.com', phone: '(818) 297-8667 License: DRE #02118210'}
394
: 
{name: 'Kevin Silver', email: 'kevin.silver@theagencyre.com', phone: '(818) 292-7222 License: DRE #1888127'}
395
: 
{name: 'Kevin Stewart', email: 'kevin.stewart@theagencyre.com', phone: '(424) 230-7807 License: DRE #02050755'}
396
: 
{name: 'Kiersten Ligeti', email: 'kiersten@theagencyre.com', phone: '(650) 766-8319 License: DRE #01298631'}
397
: 
{name: 'Kimberly Ryan', email: 'kryan@theagencyre.com', phone: '(310) 489-7064 License: DRE #01512670'}
398
: 
{name: 'Kozet Luciano', email: 'kozet.luciano@theagencyre.com', phone: '(818) 974-8886 License: DRE #1978556'}
399
: 
{name: 'Kris Everett', email: 'kris.everett@theagencyre.com', phone: '(562) 725-6458 License: DRE #02115238'}
400
: 
{name: 'Kristin Kinyon', email: 'kristin.kinyon@theagencyre.com', phone: '(925) 623-4040 License: DRE #1800467'}
401
: 
{name: 'Kristin Regan', email: 'kregan@theagencyre.com', phone: '(310) 283-3884 License: DRE #01978511'}
402
: 
{name: 'Kristina Theard', email: 'kristina.theard@theagencyre.com', phone: '(310) 245-9262 License: DRE #01939502'}
403
: 
{name: 'Kristine Lauengco', email: 'kristine.l@theagencyre.com', phone: '(213) 793-6063 License: DRE #1926329'}
404
: 
{name: 'Kyle Giese', email: 'kyle.giese@theagencyre.com', phone: '(310) 975-5838 License: DRE #1915855'}
405
: 
{name: 'Kyle Olson', email: 'kyle.olson@theagencyre.com', phone: '(949) 742-4050 License: DRE #2042708'}
406
: 
{name: 'Lala Boghzi', email: 'lala.boghzi@theagencyre.com', phone: '(818) 491-8630 License: DRE #2075442'}
407
: 
{name: 'Laura Finley', email: 'laura@theagencyre.com', phone: '(541) 601-3286 License: DRE #1973617'}
408
: 
{name: 'Laura Law', email: 'llaw@theagencyre.com', phone: '(626) 888-2640 License: DRE #02017252'}
409
: 
{name: 'Laura McNulty', email: 'laura.mcnulty@theagencyre.com', phone: '(310) 944-0555 License: DRE #02016531'}
410
: 
{name: 'Laura Shockley', email: 'laura.shockley@theagencyre.com', phone: '(310) 663-9117 License: DRE #2092374'}
411
: 
{name: 'Laura Stupsker', email: 'lstupsker@theagencyre.com', phone: '(424) 230-3735 License: DRE #01796518'}
412
: 
{name: 'Lauren Campopiano', email: 'lauren.c@theagencyre.com', phone: '(925) 575-8000 License: DRE #02137093'}
413
: 
{name: 'Lauren Grauman', email: 'lgrauman@theagencyre.com', phone: '(310) 467-5926 License: DRE #01738453'}
414
: 
{name: 'LeAnne Thrasher-Chang', email: 'leanne@theagencyre.com', phone: '(424) 400-5924 License: DRE #01896013'}
415
: 
{name: 'Leo Medeiros', email: 'leo.medeiros@theagencyre.com', phone: '(415) 305-3351 License: DRE #00933786'}
416
: 
{name: 'Leslie Rae', email: 'Bega', phone: 'leslie.bega@theagencyre.com (310) 600-6615 License: DRE #01783962'}
417
: 
{name: 'Levon Arzumanyan', email: 'levon.a@theagencyre.com', phone: '(213) 414-8088 License: DRE #01836944'}
418
: 
{name: 'Lidia Carter', email: 'lidia.carter@theagencyre.com', phone: '(650) 315-5403 License: DRE # 02206491'}
419
: 
{name: 'Lilian Hairabedian', email: 'lilian.h@theagencyre.com', phone: '(626) 497-4414 License: DRE #2045198'}
420
: 
{name: 'Lina Holub', email: 'lina.holub@theagencyre.com', phone: '(213) 922-0822 License: DRE # 02138240'}
421
: 
{name: 'Lindsay Guttman', email: 'lguttman@theagencyre.com', phone: '(424) 400-5914 License: DRE #1901278'}
422
: 
{name: 'Lindsay Hecker', email: 'lindsay.hecker@theagencyre.com', phone: '(818) 379-7117 License: DRE #02050425'}
423
: 
{name: 'Lindsay Nelms', email: 'lindsay.nelms@theagencyre.com', phone: '(760) 520-4905 License: DRE # 02063307'}
424
: 
{name: 'Lindsey Darling', email: 'lindsey.darling@theagencyre.com', phone: '(626) 639-8300 License: DRE #02054846'}
425
: 
{name: 'Lisa Ashworth', email: 'lisa.ashworth@theagencyre.com', phone: '(626) 644-3844 License: DRE #01330150'}
426
: 
{name: 'Lisa Mackie', email: 'lisa.mackie@theagencyre.com', phone: '(415) 601-5871 License: DRE #02151134'}
427
: 
{name: 'Lisa Marie', email: 'Manifold', phone: 'lisa.manifold@theagencyre.com (925) 383-9797 License: DRE #01470992'}
428
: 
{name: 'Loran Arvizu', email: 'loran.arvizu@theagencyre.com', phone: '(760) 641-5939 License: DRE #02030233'}
429
: 
{name: 'Lucio Bernal', email: 'lucio.bernal@theagencyre.com', phone: '(310) 383-2466 License: DRE #01236217'}
430
: 
{name: 'Luis Segura', email: 'luis.segura@theagencyre.com', phone: '(626) 233-2884 License: DRE #01305186'}
431
: 
{name: 'Lynn North', email: 'l.north@theagencyre.com', phone: '(650) 703-6437 License: DRE #01490039'}
432
: 
{name: 'Lytel Young', email: 'lytelyoung@theagencyre.com', phone: '(323) 646-8475 License: DRE #01710150'}
433
: 
{name: 'Madison Buffardi', email: 'madison.buffardi@theagencyre.com', phone: '(424) 230-3700 License: DRE #02135685'}
434
: 
{name: 'Madison Conliff', email: 'madison.conliff@theagencyre.com', phone: '(574) 551-9843 License: DRE #02156877'}
435
: 
{name: 'Malyn Dahlin', email: 'malyn.dahlin@theagencyre.com', phone: '(310) 773-1107 License: DRE #02036877'}
436
: 
{name: 'Manuel Sanchez', email: 'manuel.sanchez@theagencyre.com', phone: '(619) 874-1044 License: DRE #02018479'}
437
: 
{name: 'Marc Silver', email: 'msilver@theagencyre.com', phone: '(310) 809-4656 License: DRE #01875513'}
438
: 
{name: 'Marc Victor', email: 'marc.victor@theagencyre.com', phone: '(424) 522-3546 License: DRE #02167262'}
439
: 
{name: 'Marcella Hudson', email: 'marcella.hudson@theagencyre.com', phone: '(310) 707-7439 License: DRE #02144392'}
440
: 
{name: 'Marcie Sabatella', email: 'marcie.sabatella@theagencyre.com', phone: '(626) 807-9394 License: DRE #01985768'}
441
: 
{name: 'Marco Rufo', email: 'marco@theagencyre.com', phone: '(310) 488-6914 License: DRE #1362095'}
442
: 
{name: 'Margaret Combs', email: 'margaret.combs@theagencyre.com', phone: '(925) 876-6935 License: DRE #1361329'}
443
: 
{name: 'Margaret Redemer', email: 'margaret.redemer@theagencyre.com', phone: '(925) 389-1380 License: DRE #1383964'}
444
: 
{name: 'Margaret Shendal', email: 'margaret.shendal@theagencyre.com', phone: '(310) 274-8723 License: DRE #01464329'}
445
: 
{name: 'Margaret Sievers', email: 'maggie.sievers@theagencyre.com', phone: '(310) 948-1860 License: DRE #02074753'}
446
: 
{name: 'Margaux Gibson', email: 'margaux.gibson@theagencyre.com', phone: '(626) 437-4665 License: DRE #02166285'}
447
: 
{name: 'Maria Fernanda', email: 'Castro', phone: 'maria.fernanda-castro@theagencyre.com (619) 206-1290 License: DRE #02024767'}
448
: 
{name: 'Maria Grazia', email: 'Heller', phone: 'maria.heller@theagencyre.com (603) 809-1370 License: DRE #02107964'}
449
: 
{name: 'Mario Andrighetto', email: 'mario.a@theagencyre.com', phone: '(650) 796-4902 License: DRE #01993000'}
450
: 
{name: 'Mario-Armando Aceves', email: 'm.aceves@theagencyre.com', phone: '(310) 339-9510 License: DRE #02026114'}
451
: 
{name: 'Mark Choi', email: 'markpchoi@theagencyre.com', phone: '(510) 381-1116 License: DRE #01433100'}
452
: 
{name: 'Mark Dwelle', email: 'mark.dwelle@theagencyre.com', phone: '(408) 910-1362 License: DRE #01436775'}
453
: 
{name: 'Mark Kennedy', email: 'mark.kennedy@theagencyre.com', phone: '(925) 321-5296 License: DRE #1881234'}
454
: 
{name: 'Mark Tate', email: 'mark.tate@theagencyre.com', phone: '(707) 337-2057 License: DRE #01321104'}
455
: 
{name: 'Marko Lukich', email: 'marko.lukich@theagencyre.com', phone: '(323) 926-8158 License: DRE #02059224'}
456
: 
{name: 'Martha Hunt', email: 'mhunt@theagencyre.com', phone: '(310) 869-5203 License: DRE #1058657'}
457
: 
{name: 'Mary Bonham', email: 'mary.bonham@theagencyre.com', phone: '(925) 997-1787 License: DRE #01203856'}
458
: 
{name: 'Mary Hellmund', email: 'mhellmund@theagencyre.com', phone: '(424) 230-7806 License: DRE #01920353'}
459
: 
{name: 'Mary Rozatti', email: 'mary.rozatti@theagencyre.com', phone: '(949) 652-7755 License: DRE #1763684'}
460
: 
{name: 'Mary Ellen', email: 'Mancino', phone: 'me.mancino@theagencyre.com (925) 708-2800 License: DRE #01279164'}
461
: 
{name: 'Massimo Cossu', email: 'massimo.cossu@theagencyre.com', phone: '(424) 230-4918 License: DRE #02168581'}
462
: 
{name: 'Matan Michael', email: 'matan.michael@theagencyre.com', phone: '(424) 466-4700 License: DRE #2076692'}
463
: 
{name: 'Matt Lionetti', email: 'Managing', phone: 'Director matt.lionetti@theagencyre.com (647) 368-6167'}
464
: 
{name: 'Matthew Ruttenberg', email: 'mruttenberg@theagencyre.com', phone: '(310) 776-0471 License: DRE #02013915'}
465
: 
{name: 'Mauricio Umansky', email: 'mumansky@theagencyre.com', phone: '(424) 230-3701 License: DRE #1222825'}
466
: 
{name: 'Max Goltz', email: 'max.goltz@theagencyre.com', phone: '(818) 251-0802 License: DRE #01993985'}
467
: 
{name: 'Maxim Sidelnik', email: 'maximsidelnik@theagencyre.com', phone: '(818) 212-9863 License: DRE # 02109488'}
468
: 
{name: 'May Nachum', email: 'may.nachum@theagencyre.com', phone: '(818) 355-6592 License: DRE # 02205399'}
469
: 
{name: 'Media Moussavy', email: 'mmoussavy@theagencyre.com', phone: '(626) 625-9650 License: DRE #01946821'}
470
: 
{name: 'Meg Cerecedes', email: 'meg.cerecedes@theagencyre.com', phone: '(818) 631-8641 License: DRE #02132847'}
471
: 
{name: 'Megan DeVivo', email: 'megan.devivo@theagencyre.com', phone: '(831) 207-6060 License: DRE #01924071'}
472
: 
{name: 'Meir Kroll', email: 'meir@theagencyre.com', phone: '(310) 341-4393 License: DRE #01864039'}
473
: 
{name: 'Melanie Goldberger', email: 'mgoldberger@theagencyre.com', phone: '(310) 560-5895 License: DRE #1988672'}
474
: 
{name: 'Melanie Nicora', email: 'melanie.nicora@theagencyre.com', phone: '(831) 236-6842 License: DRE #942626'}
475
: 
{name: 'Melanie Welch', email: 'melanie.w@theagencyre.com', phone: '(818) 290-6911 License: DRE #01983774'}
476
: 
{name: 'Melissa Platt', email: 'melissa@theagencyre.com', phone: '(424) 230-7429 License: DRE #01961560'}
477
: 
{name: 'Melissa Siegel', email: 'melissa.siegel@theagencyre.com', phone: '(818) 822-6222 License: DRE #02039001'}
478
: 
{name: 'Melody Rabbani', email: 'melody.rabbani@theagencyre.com', phone: '(818) 943-1815 License: DRE # 02049590'}
479
: 
{name: 'Mercedes Javid', email: 'mercedesj@theagencyre.com', phone: '(310) 486-2286 License: DRE #01339234'}
480
: 
{name: 'Mica Belzberg', email: 'mica.belzberg@theagencyre.com', phone: '(310) 663-3701 License: DRE #01364864'}
481
: 
{name: 'Michael Bloom', email: 'michael.bloom@theagencyre.com', phone: '(818) 207-2088 License: DRE #01188440'}
482
: 
{name: 'Michael Caruso', email: 'michael.caruso@theagencyre.com', phone: '(949) 584-2300 License: DRE #1073919'}
483
: 
{name: 'Michael Grady', email: 'mgrady@theagencyre.com', phone: '(310) 995-8774 License: DRE #1505317'}
484
: 
{name: 'Michael Jimenez', email: 'michael.j@theagencyre.com', phone: '(916) 548-5203 License: DRE #02017030'}
485
: 
{name: 'Michael Ketring', email: 'michael.ketring@theagencyre.com', phone: '(805) 657-3855 License: DRE #01998560'}
486
: 
{name: 'Michael Meza', email: 'mike.meza@theagencyre.com', phone: '(831) 578-4601'}
487
: 
{name: 'Michael Schwartz', email: 'mike.schwartz@theagencyre.com', phone: '(510) 295-7622 License: DRE #1711786'}
488
: 
{name: 'Michael Sowa', email: 'michael.sowa@theagencyre.com', phone: '(424) 786-8512 License: DRE #02200754'}
489
: 
{name: 'Michael Williams', email: 'michael.williams@theagencyre.com', phone: '(818) 308-5620 License: DRE #1266428'}
490
: 
{name: 'Michelle Ficarra', email: 'mficarra@theagencyre.com', phone: '(310) 502-4800 License: DRE #01064276'}
491
: 
{name: 'Michelle Knutson', email: 'michelle.knutson@theagencyre.com', phone: '(818) 621-3202 License: DRE #2103223'}
492
: 
{name: 'Michelle Meyers', email: 'michelle.meyers@theagencyre.com', phone: '(818) 416-9196 License: DRE #01450380'}
493
: 
{name: 'Michelle Murphy', email: 'michelle.murphy@theagencyre.com', phone: '(310) 924-5829 License: DRE #02042842'}
494
: 
{name: 'Michelle Schwartz', email: 'mschwartz@theagencyre.com', phone: '(424) 230-3716 License: DRE #1889141'}
495
: 
{name: 'Michelle Ye', email: 'michelle.ye@theagencyre.com', phone: '(415) 312-6688 License: DRE #01758904'}
496
: 
{name: 'Miguel Aguirre', email: 'miguel.aguirre@theagencyre.com', phone: '(619) 748-5582 License: DRE #02133247'}
497
: 
{name: 'Mike Bary', email: 'mike.bary@theagencyre.com', phone: '(310) 497-9100 License: DRE #02040981'}
498
: 
{name: 'Mike Wagner', email: 'mike.wagner@theagencyre.com', phone: '(424) 302-7205 License: DRE #2044304'}
499
: 
{name: 'Minna Maselka', email: 'minna@theagencyre.com', phone: '(512) 415-2226 License: DRE #2150702'}
500
: 
{name: 'Minoti Merchant', email: 'minoti.merchant@theagencyre.com', phone: '(408) 373-7042 License: DRE #01977488'}
501
: 
{name: 'Mireya Rodriguez', email: 'mireya@theagencyre.com', phone: '(310) 606-0108 License: DRE #01922313'}
502
: 
{name: 'Miriam Bolber', email: 'miriam.bolber@theagencyre.com', phone: '(213) 260-1415 License: DRE #01922607'}
503
: 
{name: 'Misha Ford', email: 'misha.ford@theagencyre.com', phone: '(424) 203-1188 License: DRE #01182516'}
504
: 
{name: 'Mojgan Nematollahi', email: 'mojgan.n@theagencyre.com', phone: '(408) 221-7567 License: DRE #02153703'}
505
: 
{name: 'Monica Yekani', email: 'monica.yekani@theagencyre.com', phone: '(818) 431-0467 License: DRE #01994120'}
506
: 
{name: 'Monika Gabisi', email: 'mgabisi@theagencyre.com', phone: '(213) 840-6670 License: DRE #02082917'}
507
: 
{name: 'Monika Matson', email: 'monika.matson@theagencyre.com', phone: '(949) 742-0047 License: DRE #01734388'}
508
: 
{name: 'Monika Sala', email: 'monika.sala@theagencyre.com', phone: '(312) 404-0053 License: DRE #02133930'}
509
: 
{name: 'Monique Navarro', email: 'monique@theagencyre.com', phone: '(424) 354-2674 License: DRE #01978781'}
510
: 
{name: 'Morgan Goldberg', email: 'morgang@theagencyre.com', phone: '(917) 224-9908 License: DRE #02179983'}
511
: 
{name: 'Myra Arbabi', email: 'myra.arbabi@theagencyre.com', phone: '(818) 451-9550 License: DRE #01209492'}
512
: 
{name: 'Nancy Palmer', email: 'nancy.palmer@theagencyre.com', phone: '(650) 492-0200 License: DRE #00525350'}
513
: 
{name: 'Narine Avanessian', email: 'narine.avanessian@theagencyre.com', phone: '(818) 515-6338 License: DRE #2158445'}
514
: 
{name: 'Natalee Tappin', email: 'natalee.tappin@theagencyre.com', phone: '(707) 481-5653 License: DRE #02076160'}
515
: 
{name: 'Natalie Amir', email: 'natalie.amir@theagencyre.com', phone: '(747) 250-7433 License: DRE #01911260'}
516
: 
{name: 'Natalie Auermann', email: 'natalie.a@theagencyre.com', phone: '(502) 415-8119 License: DRE #02208042'}
517
: 
{name: 'Natalie Cadoch', email: 'natalie.cadoch@theagencyre.com', phone: '(310) 854-9974 License: DRE #01908355'}
518
: 
{name: 'Natalie Courtright', email: 'natalie.courtright@theagencyre.com', phone: '(312) 468-7758 License: DRE #02138484'}
519
: 
{name: 'Natalie Hadek', email: 'natalie.hadek@theagencyre.com', phone: '(805) 236-3987 License: DRE #2135454'}
520
: 
{name: 'Natalie Kouzouyan', email: 'nataliek@theagencyre.com', phone: '(949) 606-2819 License: DRE #02191650'}
521
: 
{name: 'Natalyt Estrada', email: 'natalyt.estrada@theagencyre.com', phone: '(323) 599-2200 License: DRE #02208717'}
522
: 
{name: 'Natasha Sizlo', email: 'natasha.sizlo@theagencyre.com', phone: '(424) 400-5942 License: DRE #1982402'}
523
: 
{name: 'Nathalie Giragossian', email: 'nathalie@theagencyre.com', phone: '(310) 905-2603 License: DRE #01983376'}
524
: 
{name: 'Navid Khayyat', email: 'navid.khayyat@theagencyre.com', phone: '(619) 520-0322 License: DRE #02080768'}
525
: 
{name: 'Nayeli Noyola', email: 'nayeli.noyola@theagencyre.com', phone: '(619) 227-3509 License: DRE #02109180'}
526
: 
{name: 'Neeta Gupta', email: 'neetagupta@theagencyre.com', phone: '(818) 300-5255 License: DRE # 01127029'}
527
: 
{name: 'Nelly Beck', email: 'nelly.beck@theagencyre.com', phone: '(760) 898-2979 License: DRE #2071197'}
528
: 
{name: 'Nene Murillo', email: 'nene.murillo@theagencyre.com', phone: '(510) 305-0574'}
529
: 
{name: 'Nhi Le', email: 'nhi.le@theagencyre.com', phone: '(424) 531-9934 License: DRE #02044747'}
530
: 
{name: 'Nia Harris', email: 'nia.harris@theagencyre.com', phone: '(818) 926-1357 License: DRE #2001034'}
531
: 
{name: 'Nick Collins', email: 'nick@theagencyre.com', phone: '(424) 285-1955 License: DRE #01922418'}
532
: 
{name: 'Nick Hertz', email: 'nick.hertz@theagencyre.com', phone: '(424) 285-8746 License: DRE #01992715'}
533
: 
{name: 'Nick Sandler', email: 'nick.sandler@theagencyre.com', phone: '(424) 320-9334 License: DRE #02003365'}
534
: 
{name: 'Nicky Fleming', email: 'nicky.fleming@theagencyre.com', phone: '(714) 912-9599 License: DRE #2025543'}
535
: 
{name: 'Nicole Ferland', email: 'nicole.ferland@theagencyre.com', phone: '(925) 818-8750 License: DRE #02182782'}
536
: 
{name: 'Nicole Nichols', email: 'nicole.nichols@theagencyre.com', phone: '(818) 825-7286 License: DRE # 01417053'}
537
: 
{name: 'Nicole Tekiela', email: 'nicole.tekiela@theagencyre.com', phone: '(310) 987-1701 License: DRE #2091565'}
538
: 
{name: 'Nikki Abish', email: 'nikki.abish@theagencyre.com', phone: '(818) 219-1250 License: DRE #01844904'}
539
: 
{name: 'Nikki Joel', email: 'nikki.joel@theagencyre.com', phone: '(310) 428-2248 License: DRE #1784589'}
540
: 
{name: 'Niko Corado', email: 'ncorado@theagencyre.com', phone: '(310) 918-8369 License: DRE #02016810'}
541
: 
{name: 'Nima Sajadi', email: 'nsajadi@theagencyre.com', phone: '(310) 995-6968 License: DRE #1801102'}
542
: 
{name: 'Nina Ragovski', email: 'nina.ragovski@theagencyre.com', phone: '(917) 803-2853 License: DRE #2106698'}
543
: 
{name: 'Nino Gaetano', email: 'nino.g@theagencyre.com', phone: '(650) 207-1986 License: DRE #01236316'}
544
: 
{name: 'Nisha Sharma', email: 'nisha.s@theagencyre.com', phone: '(650) 492-9263 License: DRE # 01746077'}
545
: 
{name: 'Noah Bradley', email: 'nbradley@theagencyre.com', phone: '(734) 904-3518 License: DRE #02141284'}
546
: 
{name: 'Noah Matthew', email: 'noah.matthew@theagencyre.com', phone: '(415) 678-7131 License: DRE #01941818'}
547
: 
{name: 'Nory Chin', email: 'nory.chin@theagencyre.com', phone: '(707) 718-6126 License: DRE #02079926'}
548
: 
{name: 'Olga Collatin', email: 'olga.collatin@theagencyre.com', phone: '(310) 936-1694 License: DRE #01324954'}
549
: 
{name: 'Pam Blackman', email: 'pam.blackman@theagencyre.com', phone: '(650) 823-0308 License: DRE #00584333'}
550
: 
{name: 'Pamela Rich', email: 'pamela.rich@theagencyre.com', phone: '(310) 666-7424 License: DRE #01262935'}
551
: 
{name: 'Pate Stevens', email: 'pate.stevens@theagencyre.com', phone: '(310) 467-7253 License: DRE #01749421'}
552
: 
{name: 'Patricia Barry', email: 'patty.barry@theagencyre.com', phone: '(925) 382-5824 License: DRE #00902495'}
553
: 
{name: 'Patricia Karoubi', email: 'patricia@theagencyre.com', phone: '(650) 868-4565 License: DRE #01396914'}
554
: 
{name: 'Paul Lester', email: 'plester@theagencyre.com', phone: '(310) 488-5962 License: DRE #01338925'}
555
: 
{name: 'Paul Weiler', email: 'paul.weiler@theagencyre.com', phone: '(925) 963-6452 License: DRE #1320301'}
556
: 
{name: 'Penelope Stipanovich', email: 'penelope.s@theagencyre.com', phone: '(212) 518-6233 License: DRE #2024827'}
557
: 
{name: 'Peter DiVito', email: 'pdivito@theagencyre.com', phone: '(818) 942-4262 License: DRE #01940016'}
558
: 
{name: 'Peter Mac', email: 'pmac@theagencyre.com', phone: '(424) 231-2412 License: DRE #01963649'}
559
: 
{name: 'Phillip Caruso', email: 'phillip.caruso@theagencyre.com', phone: '(949) 293-7334 License: DRE #1934516'}
560
: 
{name: 'Pompeyo Barragan', email: 'pompeyo.barragan@theagencyre.com', phone: '(619) 646-0566 License: DRE #01834839'}
561
: 
{name: 'Quetzal Grimm', email: 'quetzal@theagencyre.com', phone: '(650) 400-7879 License: DRE #01405453'}
562
: 
{name: 'Rachel Guerin,', email: 'CRP', phone: 'rachel.guerin@theagencyre.com (916) 215-0566 License: DRE #1198318'}
563
: 
{name: 'Raini Casados', email: 'rcasados@theagencyre.com', phone: '(424) 231-2413 License: DRE #1515350'}
564
: 
{name: 'Ramesh Yedidsion', email: 'ramesh@theagencyre.com', phone: '(310) 866-9399 License: DRE #00832675'}
565
: 
{name: 'Ramiro Rivas', email: 'rrivas@theagencyre.com', phone: '(626) 497-4606 License: DRE #01406511'}
566
: 
{name: 'Raul Cañada', email: 'raul.canada@theagencyre.com', phone: '(818) 274-9184 License: DRE #02165110'}
567
: 
{name: 'Raul Chavez', email: 'raul.chavez@theagencyre.com', phone: '(619) 601-1705 License: DRE #02108043'}
568
: 
{name: 'R. Austin', email: 'Brasch', phone: 'austin.brasch@theagencyre.com (310) 487-2707 License: DRE # 01980889'}
569
: 
{name: 'Rawley Valverde', email: 'rawley.valverde@theagencyre.com', phone: '(310) 339-5255 License: DRE #02024649'}
570
: 
{name: 'Ray Akbari', email: 'ray.a@theagencyre.com', phone: '(818) 400-4344 License: DRE #1447600'}
571
: 
{name: 'Raz Reichfeld', email: 'razr@theagencyre.com', phone: '(818) 612-8283 License: DRE #01290312'}
572
: 
{name: 'Razza Razon', email: 'razza.razon@theagencyre.com', phone: '(818) 635-2477 License: DRE #02042856'}
573
: 
{name: 'Rebekah Schwartz', email: 'Sklar', phone: 'rebekah@theagencyre.com (818) 449-0172 License: DRE #01215678'}
574
: 
{name: 'René Wiebensohn', email: 'rene.w@theagencyre.com', phone: '(323) 797-0858 License: DRE #01942621'}
575
: 
{name: 'Renee Spooner', email: 'renee.spooner@theagencyre.com', phone: '(650) 477-5484 License: DRE #02208188'}
576
: 
{name: 'Ricarda Olander', email: 'ricarda.olander@theagencyre.com', phone: '(424) 431-7237 License: DRE #02140400'}
577
: 
{name: 'Ricardo Beer', email: 'ricardo@theagencyre.com', phone: '(424) 283-4984 License: DRE #1960919'}
578
: 
{name: 'Rich Mejia', email: 'rich.mejia@theagencyre.com', phone: '(818) 606-6549 License: DRE # 02048283'}
579
: 
{name: 'Richard Wilkinson', email: 'richard.wilkinson@theagencyre.com', phone: '(323) 445-2426 License: DRE #01812487'}
580
: 
{name: 'Rick Dunne', email: 'rick.dunne@theagencyre.com', phone: '(925) 325-0292'}
581
: 
{name: 'Rick Zea', email: 'rick.zea@theagencyre.com', phone: '(408) 205-8050 License: DRE #00880772'}
582
: 
{name: 'Rishi Kumar', email: 'rkumar@theagencyre.com', phone: '(424) 230-3708 License: DRE #1922777'}
583
: 
{name: 'Rita Whitney', email: 'rjwhitney@theagencyre.com', phone: '(626) 755-4988 License: DRE #01209004'}
584
: 
{name: 'Rob Sandefer', email: 'robert.sandefer@theagencyre.com', phone: '(310) 889-8463 License: DRE #01996491'}
585
: 
{name: 'Robert Lee', email: 'robert.lee@theagencyre.com', phone: '(323) 394-6815 License: DRE #1936075'}
586
: 
{name: 'Robin Gaur', email: 'robin.gaur@theagencyre.com', phone: '(818) 836-8337 License: DRE #01832992'}
587
: 
{name: 'Robin Gordon', email: 'robin.gordon@theagencyre.com', phone: '(707) 291-7952 License: DRE #01883212'}
588
: 
{name: 'Roger Gendron', email: 'roger.gendron@theagencyre.com', phone: '(818) 571-4390 License: DRE #01968062'}
589
: 
{name: 'Romina Minassian', email: 'romina.minassian@theagencyre.com', phone: '(818) 381-3757 License: DRE #2061222'}
590
: 
{name: 'Ron Shapiro', email: 'ron.shapiro@theagencyre.com', phone: '(818) 665-5255 License: DRE #02169025'}
591
: 
{name: 'Ronnie Jenkins', email: 'ronnie.jenkins@theagencyre.com', phone: '(949) 409-5571 License: DRE # 01922959'}
592
: 
{name: 'Rosalie Klein', email: 'rosalie@theagencyre.com', phone: '(310) 261-8878 License: DRE #1115025'}
593
: 
{name: 'Rossy Leon', email: 'Hernandez', phone: 'rossy@theagencyre.com (310) 849-9793 License: DRE #2107802'}
594
: 
{name: 'Rouja Koleva', email: 'rouja@theagencyre.com', phone: '(310) 977-8202 License: DRE #01936334'}
595
: 
{name: 'Ruben Valerio', email: 'ruben.valerio@theagencyre.com', phone: '+52 81 8903 9479 License: DRE #02096100'}
596
: 
{name: 'Rurik Best', email: 'r.best@theagencyre.com', phone: '(310) 862-0012'}
597
: 
{name: 'Ruslan Shkurenko', email: 'ruslan@theagencyre.com', phone: '(424) 333-6967 License: DRE #2096208'}
598
: 
{name: 'Ryan Gowdy', email: 'ryan.gowdy@theagencyre.com', phone: '(408) 309-8660 License: DRE #01322889'}
599
: 
{name: 'Ryan King', email: 'ryan.king@theagencyre.com', phone: '(310) 850-6058 License: DRE #01955101'}
600
: 
{name: 'Sabrina Vallejos', email: 'sabrina.vallejos@theagencyre.com', phone: '(310) 926-5711 License: DRE #2041007'}
601
: 
{name: 'Sacha Radford', email: 'sacha@theagencyre.com', phone: '(310) 617-4464 License: DRE #1404368'}
602
: 
{name: 'Saena Hart', email: 'saena.hart@theagencyre.com', phone: '(626) 460-0675 License: DRE #02049322'}
603
: 
{name: 'Safia Lasman', email: 's.lasman@theagencyre.com', phone: '(760) 269-3185 License: DRE #2072606'}
604
: 
{name: 'Sam Collins', email: 'sam.collins@theagencyre.com', phone: '(424) 777-5135 License: DRE #02057606'}
605
: 
{name: 'Sam Palmer', email: 'sam.palmer@theagencyre.com', phone: '(310) 925-3337 License: DRE #02146357'}
606
: 
{name: 'Sam Weinberger', email: 'sam.weinberger@theagencyre.com', phone: '(818) 400-1747 License: DRE #02015949'}
607
: 
{name: 'Samira Gores', email: 'sgores@theagencyre.com', phone: '(310) 405-9244 License: DRE #1323193'}
608
: 
{name: 'Samira Guirguis', email: 'samira.guirguis@theagencyre.com', phone: '(310) 980-3422 License: DRE #1819096'}
609
: 
{name: 'Sammi Moser-Wingo', email: 'sammi.moser@theagencyre.com', phone: '(408) 857-2026 License: DRE #01949758'}
610
: 
{name: 'Sandra Luesse', email: 'sandra.luesse@theagencyre.com', phone: '(949) 405-3120 License: DRE #2110741'}
611
: 
{name: 'Sandro Dazzan', email: 'sandro@theagencyre.com', phone: '(424) 249-7040 License: DRE #1418033'}
612
: 
{name: 'Santiago Arana', email: 'santiago@theagencyre.com', phone: '(424) 231-2399 License: DRE #01492489'}
613
: 
{name: 'Sara Joata', email: 'sara.joata@theagencyre.com', phone: '(949) 610-3773 License: DRE #02168012'}
614
: 
{name: 'Sara Sandefer', email: 'sara.sandefer@theagencyre.com', phone: '(805) 689-7129 License: DRE #01898641'}
615
: 
{name: 'Sarah Asaly', email: 'sarah.asaly@theagencyre.com', phone: '(949) 303-8785 License: DRE #02091833'}
616
: 
{name: 'Sarah Knauer', email: 'sarahk@theagencyre.com', phone: '(310) 663-4606 License: DRE #01939773'}
617
: 
{name: 'Sarrah Gallegos', email: 'sarrah.gallegos@theagencyre.com', phone: '(818) 269-3222 License: DRE #02077086'}
618
: 
{name: 'Scott Gorelick', email: 'scottg@theagencyre.com', phone: '(310) 600-2511 License: DRE #01876674'}
619
: 
{name: 'Scott Wynne', email: 'scott.wynne@theagencyre.com', phone: '(310) 467-1369 License: DRE #01291071'}
620
: 
{name: 'Sean Mauser', email: 'sean.mauser@theagencyre.com', phone: '(925) 791-0440 License: DRE #01369766'}
621
: 
{name: 'Sebastian Spader', email: 'sspader@theagencyre.com', phone: '(310) 995-9700 License: DRE #02013827'}
622
: 
{name: 'Sergio El-Azzi', email: 'sergio.elazzi@theagencyre.com', phone: '(647) 204-1802'}
623
: 
{name: 'Sevak Isayan', email: 'sev.isayan@theagencyre.com', phone: '(818) 378-1883 License: DRE #1837895'}
624
: 
{name: 'Shane Farkas', email: 'shane@theagencyre.com', phone: '(424) 230-3745 License: DRE #1711165'}
625
: 
{name: 'Shane Willcox', email: 'shane.willcox@theagencyre.com', phone: '(310) 962-7443 License: DRE #01978241'}
626
: 
{name: 'Shannon Vital', email: 'shay@theagencyre.com', phone: '(310) 993-8028 License: DRE #1510343'}
627
: 
{name: 'Sharlene Gerus', email: 'sharlene.gerus@theagencyre.com', phone: '(310) 895-5847 License: DRE #02173192'}
628
: 
{name: 'Sharon Gill', email: 'sharon.gill@theagencyre.com', phone: '(415) 355-4797 License: DRE #02036831'}
629
: 
{name: 'Sharon Umansky', email: 'Benton', phone: 'sharon.benton@theagencyre.com (310) 383-5455 License: DRE #02021318'}
630
: 
{name: 'Sheila Etheridge', email: 'sheila.e@theagencyre.com', phone: '(858) 248-5453 License: DRE #01428796'}
631
: 
{name: 'Shilpa Merchant', email: 'shilpa.merchant@theagencyre.com', phone: '(650) 906-6869 License: DRE #01112533'}
632
: 
{name: 'Shirley Moalem', email: 'shirley.moalem@theagencyre.com', phone: '(818) 357-7200 License: DRE #01986365'}
633
: 
{name: 'Shoshana Shamoeil', email: 'shoshana@theagencyre.com', phone: '(310) 717-6558 License: DRE #02045971'}
634
: 
{name: 'Shylee Halimi', email: 'shylee.halimi@theagencyre.com', phone: '(818) 288-4931 License: DRE #02021043'}
635
: 
{name: 'Simin Tabibnia', email: 'simin@theagencyre.com', phone: '(310) 930-5446 License: DRE #01983428'}
636
: 
{name: 'Soli Saatchi', email: 'soli.saatchi@theagencyre.com', phone: '(650) 996-9364 License: DRE #00925744'}
637
: 
{name: 'Sonia Cabrera', email: 'sonia.cabrera@theagencyre.com', phone: '(818) 602-6882 License: DRE #01748974'}
638
: 
{name: 'Sonika Vaid', email: 'sonika.vaid@theagencyre.com', phone: '(424) 210-3109 License: DRE #02091450'}
639
: 
{name: 'Sophia Hirjee', email: 'sophia.hirjee@theagencyre.com', phone: '(310) 895-3556 License: DRE #02114235'}
640
: 
{name: 'Sophia Kelley', email: 'sophia.kelley@theagencyre.com', phone: '(818) 235-6623 License: DRE #01962713'}
641
: 
{name: 'Stefan Pommepuy', email: 'stefan@theagencyre.com', phone: '(310) 562-6264 License: DRE #1817077'}
642
: 
{name: 'Stephanie DeCarlo', email: 'sdecarlo@theagencyre.com', phone: '(323) 401-0634 License: DRE #02094862'}
643
: 
{name: 'Stephanie Dunn', email: 'stephanie.dunn@theagencyre.com', phone: '(760) 410-9037 License: DRE #02078582'}
644
: 
{name: 'Stephanie Van', email: 'Ostrander', phone: 'stephanie.vanostrander@theagencyre.com (310) 908-3643 License: DRE #02139706'}
645
: 
{name: 'Stephany Delgado', email: 'stephany.delgado@theagencyre.com', phone: '(818) 472-9615 License: DRE #02003810'}
646
: 
{name: 'Stephen Katz', email: 'stephen.katz@theagencyre.com', phone: '(310) 482-9170 License: DRE #2070926'}
647
: 
{name: 'Stephen Saffold', email: 'saffold@theagencyre.com', phone: '(510) 282-9169 License: DRE #1777825'}
648
: 
{name: 'Stephen White', email: 'stephenwhite@theagencyre.com', phone: '(310) 919-6676 License: DRE # 02009880'}
649
: 
{name: 'Steve Garrett', email: 'sgarrett@theagencyre.com', phone: '(310) 890-2520 License: DRE #01991646'}
650
: 
{name: 'Steven Davis', email: 'steven.davis@theagencyre.com', phone: '(310) 801-9457 License: DRE #01969567'}
651
: 
{name: 'Steven Ejiofor', email: 'steven.ejiofor@theagencyre.com', phone: '(818) 336-7722 License: DRE #1956782'}
652
: 
{name: 'Steven Galindo', email: 'steven.galindo@theagencyre.com', phone: '(626) 639-8548 License: DRE #1002784'}
653
: 
{name: 'Steven Kirshbaum', email: 'skirshbaum@theagencyre.com', phone: '(424) 230-3743 License: DRE #1381800'}
654
: 
{name: 'Steven M.', email: 'Jones', phone: 'steven.jones@theagencyre.com (310) 488-9979 License: DRE #1836994'}
655
: 
{name: 'Sunny Fedorenko', email: 'sunny.fedorenko@theagencyre.com', phone: '(323) 899-4042 License: DRE #2095128'}
656
: 
{name: 'Susan Montgomery', email: 'susan.montgomery@theagencyre.com', phone: '(707) 695-1584 License: DRE #01107261'}
657
: 
{name: 'Susan Rejba', email: 'susan.rejba@theagencyre.com', phone: '(310) 266-7790 License: DRE #01997231'}
658
: 
{name: 'Susan Sims', email: 'susan.sims@theagencyre.com', phone: '(650) 743-1838 License: DRE #01408349'}
659
: 
{name: 'Sushma Mukku', email: 'sushma.mukku@theagencyre.com', phone: '(510) 552-2479 License: DRE #02067934'}
660
: 
{name: 'Susie Aguirre', email: 'susie.aguirre@theagencyre.com', phone: '(626) 399-4988 License: DRE #01130705'}
661
: 
{name: 'Suzannah Murphy', email: 'suzi.murphy@theagencyre.com', phone: '(424) 421-9490 License: DRE #2121177'}
662
: 
{name: "Suzanne O'Brien", email: 'suzanne.obrien@theagencyre.com', phone: '(650) 996-9898 License: DRE #01467942'}
663
: 
{name: 'Sylvia Torres', email: 'sylvia.torres@theagencyre.com', phone: '(310) 251-4160 License: DRE #02179519'}
664
: 
{name: 'Tadeh Hambarsoonian', email: 'tadeh.h@theagencyre.com', phone: '(818) 303-4446 License: DRE #02138488'}
665
: 
{name: 'Tara Holt', email: 'taraholt@theagencyre.com', phone: '(424) 234-3342 License: DRE # 02193451'}
666
: 
{name: 'Tatiana Batmanian', email: 'tatiana.b@theagencyre.com', phone: '(818) 726-2663 License: DRE # 01986103'}
667
: 
{name: 'Tatiana Dyler', email: 'tatiana.dyler@theagencyre.com', phone: '(503) 716-6211 License: DRE #02202891'}
668
: 
{name: 'Taylor Morphy', email: 'taylor.morphy@theagencyre.com', phone: '(626) 376-2086 License: DRE #01960365'}
669
: 
{name: 'Terek Kelly', email: 'terek.kelly@theagencyre.com', phone: '(424) 233-0928 License: DRE #01997450'}
670
: 
{name: 'Teresa Ruelas', email: 'teresaruelas@theagencyre.com', phone: '(646) 617-8734 License: DRE #02000893'}
671
: 
{name: 'Terri Munselle', email: 'terri.munselle@theagencyre.com', phone: '(760) 409-4560 License: DRE #01260226'}
672
: 
{name: 'Terri Yolo', email: 'terri.yolo@theagencyre.com', phone: '(707) 484-6578 License: DRE #01877521'}
673
: 
{name: 'Tessa Johnson', email: 'tessa.johnson@theagencyre.com', phone: '(424) 346-9305 License: DRE #01056486'}
674
: 
{name: 'Thomas Bruce', email: 'tom.bruce@theagencyre.com', phone: '(831) 277-7200 License: DRE #00804595'}
675
: 
{name: 'Tiffany Martin', email: 'tmartin@theagencyre.com', phone: '(424) 230-3261 License: DRE #1794840'}
676
: 
{name: 'Tina Sarafa', email: 'tina.sarafa@theagencyre.com', phone: '(310) 502-5792 License: DRE #1352711'}
677
: 
{name: 'Tom Dolezel', email: 'tom.dolezel@theagencyre.com', phone: '(310) 919-6563 License: DRE #02121377'}
678
: 
{name: 'Tommy Jordan', email: 'tommy.jordan@theagencyre.com', phone: '(760) 851-4158 License: DRE #1887038'}
679
: 
{name: 'Tony Barouti', email: 'tony.barouti@theagencyre.com', phone: '(213) 300-4300 License: DRE #1714772'}
680
: 
{name: "Tony O'Brien", email: 'tony.obrien@theagencyre.com', phone: '(631) 983-7319 License: DRE # 02200838'}
681
: 
{name: 'Tori Atwell', email: 'tori.atwell@theagencyre.com', phone: '(650) 996-0123 License: DRE #00927794'}
682
: 
{name: 'Tracy Falkson', email: 'tracy.falkson@theagencyre.com', phone: '(415) 505-4450 License: DRE #02188649'}
683
: 
{name: 'Tracy Taggart', email: 'ttaggart@theagencyre.com', phone: '(818) 203-1023 License: DRE #01480514'}
684
: 
{name: 'Travis Schenck', email: 'travis.schenck@theagencyre.com', phone: '(310) 890-9577 License: DRE #1944080'}
685
: 
{name: 'Trevor Davis', email: 'trevor.davis@theagencyre.com', phone: '(310) 730-3146 License: DRE #02204047'}
686
: 
{name: 'Trevor Zien', email: 'trevor.zien@theagencyre.com', phone: '(310) 403-8763 License: DRE #01980857'}
687
: 
{name: 'Tyler Hill', email: 'tylerhill@theagencyre.com', phone: '(323) 428-5266 License: DRE #2071063'}
688
: 
{name: 'Valeria Losiuk', email: 'valeria.losiuk@theagencyre.com', phone: '(312) 860-8379 License: DRE #2069304'}
689
: 
{name: 'Vanessa Villela', email: 'vanessa.villela@theagencyre.com', phone: '(424) 346-9309 License: DRE #02105856'}
690
: 
{name: 'Veronica Henze', email: 'veronica.henze@theagencyre.com', phone: '(310) 936-1521 License: DRE #2061230'}
691
: 
{name: 'Vicki Ferrando', email: 'vicki.f@theagencyre.com', phone: '(415) 279-6636 License: DRE #01418802'}
692
: 
{name: 'Vicky Sheng', email: 'vicky.s@theagencyre.com', phone: '(310) 903-7050 License: DRE #01738566'}
693
: 
{name: 'Victor Browne', email: 'victor.brown@theagencyre.com', phone: '(818) 924-3924 License: DRE #01937070'}
694
: 
{name: 'Victoria Velazquez', email: 'victoriav@theagencyre.com', phone: '(310) 614-4240 License: DRE #02038302'}
695
: 
{name: 'Viktor Aaberg', email: 'viktor@theagencyre.com', phone: '(424) 303-9135 License: DRE #2025636'}
696
: 
{name: 'Vincent Minelli', email: 'vincent.minelli@theagencyre.com', phone: '(510) 326-8034 License: DRE # 01926199'}
697
: 
{name: 'Vincent Morales', email: 'vincent.morales@theagencyre.com', phone: '(818) 379-7120 License: DRE #01986222'}
698
: 
{name: 'Walter Franco', email: 'walter.franco@theagencyre.com', phone: '(562) 686-6613 License: DRE #02063294'}
699
: 
{name: 'Wayne Rivas', email: 'wayne.rivas@theagencyre.com', phone: '(650) 740-5746 License: DRE #01055861'}
700
: 
{name: 'Wesley Edberg', email: 'wesley.edberg@theagencyre.com', phone: '(310) 991-8557 License: DRE #01952052'}
701
: 
{name: 'William Baker', email: 'william.baker@theagencyre.com', phone: '(310) 867-0847 License: DRE #01931658'}
702
: 
{name: 'William Cerqueira', email: 'wcerqueira@theagencyre.com', phone: '(310) 498-1843 License: DRE #01851081'}
703
: 
{name: 'Wolf Amer', email: 'wolfamer@theagencyre.com', phone: '(310) 383-3282 License: DRE #2002555'}
704
: 
{name: 'Yaileen Gamiz', email: 'yaileen.gamiz@theagencyre.com', phone: '(619) 289-1029 License: DRE # 02137818'}
705
: 
{name: 'Yonathan Baltazar', email: 'yonathan.baltazar@theagencyre.com', phone: '(213) 273-3797 License: DRE #1991889'}
706
: 
{name: 'Yoonjin Stovall', email: 'yoonjin.stovall@theagencyre.com', phone: '(714) 351-4416 License: DRE #02049222'}
707
: 
{name: 'Zach Goldsmith', email: 'zach.goldsmith@theagencyre.com', phone: '(310) 908-6860 License: DRE #01454329'}
708
: 
{name: 'Zhane Dikes', email: 'zhane.dikes@theagencyre.com', phone: '(415) 417-9774 License: DRE #02051605'}
"""

# Split the input text into individual entries
entries = re.split(r'\d+\s*:\s*\n', input_text)

# Initialize an empty list to store the formatted data
data = []

company = "The Agency RE"  # Company name

# Loop through the entries and extract information
for entry in entries:
    if not entry.strip():
        continue  # Skip empty entries
    
    entry = entry.strip()
    name = re.search(r"name:\s*'([^']+)'", entry).group(1)
    email = re.search(r"email:\s*'([^']+)'", entry).group(1)
    
    # Extract the phone number within parentheses using regex
    phone_match = re.search(r"phone:\s*'(\([^)]+\))", entry)
    phone = phone_match.group(1) if phone_match else None
    
    formatted_entry = {
        'name': name,
        'email': email,
        'phone': phone,
        'company': company  # Add the company name
    }
    
    data.append(formatted_entry)

# Define your data as a list of dictionaries
existing_data = [
]

formatted_data = existing_data + data

# Print the formatted data
for i, entry in enumerate(formatted_data):
    print(f"{i}:")
    print(entry)

# Create a DataFrame from the data
df = pd.DataFrame(formatted_data)

# Drop rows with undefined values (NaN or empty strings)
df = df.dropna(subset=['name', 'email'])

# Specify the output CSV file path
output_csv = 'california_part_5.csv'

# Save the cleaned DataFrame to a CSV file
df.to_csv(output_csv, index=False)

print(f"Cleaned data saved to '{output_csv}'")
