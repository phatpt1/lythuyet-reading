import streamlit as st

data = [
    {
        "title": "ĐỌC 1 - Passage 1: Wildlife in danger",
        "content": """Nowadays people are more aware that wildlife all over the world is in danger. Many species of animals are threatened, and could easily become _(1)_ if we do not make an effort to protect them. There are many reasons for this. In some cases, animals are hunted for their fur or for other valuable parts of their bodies. Some birds, _(2)_ as parrots are caught alive and sold as pets. For many animals and birds, the problem is that their habitat-the place where they live-is disappearing. More _(3)_ is used for farms, for houses or industry, and there are fewer open spaces than there once were. Farmers use powerful chemicals to help them grow better crops, but these chemicals pollute _(4)_ environment and harm wildlife. The most successful animal on earth-human beings-will soon be the only ones left, _(5)_ we can solve this problem.""",
        "content_vi": """Ngày nay, mọi người ngày càng nhận thức được rằng động vật hoang dã trên toàn thế giới đang gặp nguy hiểm. Nhiều loài động vật đang bị đe dọa và có thể dễ dàng bị tuyệt chủng nếu chúng ta không nỗ lực bảo vệ chúng. Có nhiều lý do cho việc này. Trong một số trường hợp, động vật bị săn bắt để lấy lông hoặc các bộ phận có giá trị khác trên cơ thể. Một số loài chim, chẳng hạn như vẹt, bị bắt sống và bán làm thú cưng. Đối với nhiều loài động vật và chim, vấn đề là môi trường sống của chúng - nơi chúng sinh sống - đang biến mất. Nhiều đất đai hơn được sử dụng cho trang trại, nhà ở hoặc công nghiệp, và có ít không gian mở hơn so với trước đây. Nông dân sử dụng hóa chất mạnh để giúp cây trồng phát triển tốt hơn, nhưng những hóa chất này làm ô nhiễm môi trường và gây hại cho động vật hoang dã. Loài động vật thành công nhất trên trái đất - con người - sẽ sớm trở thành loài duy nhất còn sót lại, trừ khi chúng ta có thể giải quyết vấn đề này.""",
        "questions": [
            {"question": "Question 1", "options": ["A. disappeared", "B. lost", "C. extinct", "D. empty"], "answer": "C. extinct"},
            {"question": "Question 2", "options": ["A. like", "B. such", "C. and", "D. or"], "answer": "B. such"},
            {"question": "Question 3", "options": ["A. soil", "B. area", "C. earth", "D. land"], "answer": "D. land"},
            {"question": "Question 4", "options": ["A. a", "B. that", "C. an", "D. the"], "answer": "D. the"},
            {"question": "Question 5", "options": ["A. unless", "B. if", "C. however", "D. because"], "answer": "A. unless"}
        ]
    },
    {
        "title": "ĐỌC 1 - Passage 2: Ben's Drums",
        "content": """Two years ago, our 14-year-old son, Ben, asked us for a set of drums for his birthday. At first, we were very much against the idea because of the noise. 'It's better than watching television or playing computer games in my free time,' Ben argued, "and it'll keep me out of trouble.' In the end we gave in. 'All right,' we said, 'but you must consider the rest of the family and the neighbors when you play.'

That was just the beginning. Because drums are not the easiest instruments to transport, the other members of Bens band started appearing at our home with their guitars and other electrical equipment. And so, for several hours a week, the house shakes to the noise of their instruments and their teenage singing.

At least Ben's hobby has been good for our health: whenever the band start practicing, my husband and I go out for a long walk. And I must admit that, although their music may sound a little strange, they are a friendly and polite group of young men. I cannot judge their musical Skill after all I didn't expect my parents generation to like the same music as I did when I was a teenager - but they do play regularly in local clubs for young people.

Our main worry is that they won't spend enough time on their school work because of their musical activities, though this hasn't happened yet. I am always stressing to Ben how important his studies are. But one thing is certain Ben was right: it has kept him out of trouble and he is never bored.""",
        "content_vi": """Hai năm trước, cậu con trai 14 tuổi của chúng tôi, Ben, đã xin chúng tôi một dàn trống nhân dịp sinh nhật. Ban đầu, chúng tôi rất phản đối ý tưởng này vì tiếng ồn. 'Nó tốt hơn là xem tivi hay chơi trò chơi điện tử vào thời gian rảnh,' Ben lập luận, 'và nó sẽ giúp con tránh xa rắc rối.' Cuối cùng chúng tôi cũng nhượng bộ. 'Được rồi,' chúng tôi nói, 'nhưng con phải nghĩ đến những người còn lại trong gia đình và hàng xóm khi con chơi.'

Đó chỉ mới là bắt đầu. Vì trống không phải là nhạc cụ dễ vận chuyển nhất, các thành viên khác trong ban nhạc của Ben bắt đầu xuất hiện tại nhà chúng tôi với đàn guitar và các thiết bị điện khác của họ. Và thế là, trong vài giờ mỗi tuần, ngôi nhà rung chuyển vì tiếng ồn từ các nhạc cụ và tiếng hát tuổi teen của họ.

Ít nhất thì sở thích của Ben cũng tốt cho sức khỏe của chúng tôi: bất cứ khi nào ban nhạc bắt đầu tập luyện, chồng tôi và tôi lại ra ngoài đi dạo một vòng dài. Và tôi phải thừa nhận rằng, mặc dù âm nhạc của họ nghe có vẻ hơi lạ, nhưng họ là một nhóm thanh niên thân thiện và lịch sự. Tôi không thể đánh giá kỹ năng âm nhạc của họ - rốt cuộc thì tôi không mong đợi thế hệ bố mẹ tôi thích cùng thể loại nhạc mà tôi thích khi còn là một thiếu niên - nhưng họ thực sự có chơi thường xuyên ở các câu lạc bộ địa phương dành cho giới trẻ.

Mối lo ngại chính của chúng tôi là họ sẽ không dành đủ thời gian cho việc học ở trường vì các hoạt động âm nhạc, mặc dù điều này chưa xảy ra. Tôi luôn nhấn mạnh với Ben rằng việc học của con quan trọng như thế nào. Nhưng có một điều chắc chắn là Ben đã đúng: nó đã giúp thằng bé tránh xa rắc rối và không bao giờ cảm thấy nhàm chán.""",
        "questions": [
            {"question": "1. What is the writer trying to do in this text?", "options": ["A. complain about her son's friends", "B. give advice to teenagers", "C. describe her son's hobby", "D. compare herself with her parents"], "answer": "C. describe her son's hobby"},
            {"question": "2. Why did the writer give Ben the present he wanted?", "options": ["A. She wanted to reward him for working hard.", "B. He already had too many computer games.", "C. She knew he would use it sensibly.", "D. He persuaded her it would be a good idea."], "answer": "D. He persuaded her it would be a good idea."},
            {"question": "3. Why do the band always practice at Ben's house?", "options": ["A. It is difficult for Ben to move his drums.", "B. The neighbors don't mind the noise.", "C. Ben's parents enjoy listening to them.", "D. They can leave their equipment there."], "answer": "A. It is difficult for Ben to move his drums."},
            {"question": "4. What does the writer say about the band members?", "options": ["A. Their influence on her son worries her.", "B. Their taste in music is different from hers.", "C. They play their instruments well.", "D. They avoid any contact with her."], "answer": "B. Their taste in music is different from hers."}
        ]
    },
    {
        "title": "ĐỌC 1 - Passage 3: Mankind and Flags",
        "content": """Mankind has used flags for over 4,000 years. The first flags were simply wooden poles with carving at the top. About 2,000 years ago, fabric was added to the poles giving the appearance of what we know today as a flag.

The flag has become an important symbol for identifying a country. Because there are thousands of flags in existence today, many look very similar. The flag of Russia consists of three horizontal stripes that are white, red, and blue from top to bottom. The flag of Yugoslavia has a similar design, with the colors in the order of red then white then blue. Colors on flags are important since they have special meanings. Red means power and white means peace. Orange is a symbol of courage or sacrifice. Green is the color of safety and hope and yellow of caution. Black is a symbol of death and often not a color used in country flags.

Symbols of flags also have meanings. The American flag has thirteen stripes, which represent the original thirteen colonies. There are also 50 stars representing 50 states in the nation. Because of the meaning that we place on our flags, they have become a symbol of our home and of ourselves.""",
        "content_vi": """Nhân loại đã sử dụng cờ hơn 4.000 năm. Những lá cờ đầu tiên chỉ đơn giản là những cột gỗ có chạm khắc ở trên cùng. Khoảng 2.000 năm trước, vải được thêm vào các cột để tạo ra hình dáng của những gì chúng ta biết ngày nay là một lá cờ.

Lá cờ đã trở thành một biểu tượng quan trọng để nhận dạng một quốc gia. Bởi vì ngày nay có hàng ngàn lá cờ tồn tại, nhiều lá cờ trông rất giống nhau. Cờ của Nga gồm ba sọc ngang màu trắng, đỏ và xanh lam từ trên xuống dưới. Cờ của Nam Tư có thiết kế tương tự, với các màu theo thứ tự đỏ, trắng, rồi xanh lam. Màu sắc trên cờ rất quan trọng vì chúng có ý nghĩa đặc biệt. Màu đỏ có nghĩa là sức mạnh và màu trắng có nghĩa là hòa bình. Màu cam là biểu tượng của lòng can đảm hoặc sự hy sinh. Màu xanh lá cây là màu của sự an toàn và hy vọng và màu vàng của sự thận trọng. Màu đen là biểu tượng của cái chết và thường không phải là màu được sử dụng trong cờ của các quốc gia.

Biểu tượng của cờ cũng có ý nghĩa. Cờ Mỹ có mười ba sọc, đại diện cho mười ba thuộc địa ban đầu. Cũng có 50 ngôi sao đại diện cho 50 bang trong quốc gia. Bởi vì ý nghĩa mà chúng ta đặt lên cờ của mình, chúng đã trở thành biểu tượng cho quê hương và bản thân chúng ta.""",
        "questions": [
            {"question": "1. According to the passage, when did the flag have its current appearance?", "options": ["A. Over 4,000 years ago", "B. About 2,000 years ago", "C. When Russia had its flag", "D. When Yugoslavia had its flag"], "answer": "B. About 2,000 years ago"},
            {"question": "2. What fact does the author say about the first known flag?", "options": ["A. They were originated in Russia", "B. They existed over 4,000 years ago.", "C. They were a symbol of courage.", "D. They were completed with a pole and fabric."], "answer": "B. They existed over 4,000 years ago."},
            {"question": "3. According to the passage, what is the color of the top stripe on the flag of Yugoslavia?", "options": ["A. White", "B. Red", "C. Blue", "D. Green"], "answer": "B. Red"},
            {"question": "4. According to the passage, what does the color red symbolize?", "options": ["A. Death", "B. Power", "C. Peace", "D. Courage"], "answer": "B. Power"},
            {"question": "5. According to the passage, what color is NOT often used on flags of countries?", "options": ["A. Black", "B. Green", "C. Pink", "D. Orange"], "answer": "A. Black"}
        ]
    },
    {
        "title": "ĐỌC 1 - Passage 4: Student Volunteers Needed",
        "content": """Student Volunteers Needed!
On Saturday, December 12th, from 10 A.M. until 4 P.M., Carverton Middle School will be holding a music festival in the school gymnasium. The special event will feature a variety of professional musicians and singers.

Task: Make posters | Time: 1 P.M.-4 P.M. | Date: December 5th
Task: Set up gym | Time: 11 A.M.-4 P.M. | Date: December 11th
Task: Help performers | Time: 9 A.M.-4 P.M. | Date: December 12th
Task: Welcome guests | Time: 10 A.M.-2 P.M. | Date: December 12th
Task: Clean up gym | Time: 4 P.M.-7 P.M. | Date: December 12th

Interested students should speak with Ms. Braxton, the music teacher. Students who would like to help at the festival must have written permission from a parent or guardian.""",
        "content_vi": """Cần Sinh Viên Tình Nguyện!
Vào Thứ Bảy, ngày 12 tháng 12, từ 10 giờ sáng đến 4 giờ chiều, Trường Trung học Carverton sẽ tổ chức một lễ hội âm nhạc tại phòng tập thể dục của trường. Sự kiện đặc biệt này sẽ có sự góp mặt của nhiều nhạc sĩ và ca sĩ chuyên nghiệp.

Nhiệm vụ: Làm áp phích | Thời gian: 1 P.M.-4 P.M. | Ngày: 5 tháng 12
Nhiệm vụ: Thiết lập phòng tập | Thời gian: 11 A.M.-4 P.M. | Ngày: 11 tháng 12
Nhiệm vụ: Giúp đỡ người biểu diễn | Thời gian: 9 A.M.-4 P.M. | Ngày: 12 tháng 12
Nhiệm vụ: Đón khách | Thời gian: 10 A.M.-2 P.M. | Ngày: 12 tháng 12
Nhiệm vụ: Dọn dẹp phòng tập | Thời gian: 4 P.M.-7 P.M. | Ngày: 12 tháng 12

Những học sinh quan tâm nên nói chuyện với cô Braxton, giáo viên âm nhạc. Những học sinh muốn giúp đỡ tại lễ hội phải có sự cho phép bằng văn bản từ phụ huynh hoặc người giám hộ.""",
        "questions": [
            {"question": "1. What time will the festival begin?", "options": ["A. 10 A.M.", "B. 11 A.M.", "C. 1 P.M.", "D. 2 P.M."], "answer": "A. 10 A.M."},
            {"question": "2. In line 3, the word feature is closest in meaning to", "options": ["A. look", "B. keep", "C. include", "D. entertain"], "answer": "C. include"},
            {"question": "3. What job will be done the day before the festival begins?", "options": ["A. Making posters", "B. Setting up the gym", "C. Cleaning up the gym", "D. Helping the performers"], "answer": "B. Setting up the gym"},
            {"question": "4. Who is told to talk to Ms. Braxton?", "options": ["A. Parents", "B. Students", "C. Teachers", "D. Performers"], "answer": "B. Students"}
        ]
    },
    {
        "title": "ĐỌC 1 - Passage 5: The New Science Teacher",
        "content": """When the spring semester began, students at Eastern High School were met by a new science teacher. Her name is Elaine Burgess, and she has replaced Donald Young, who retired to spend time with his grandchildren.

Since Ms. Burgess has just started here, many students are curious about her background. She was kind enough to sit down for an interview with The Quill and Paper. According to Ms. Burgess, she received her master's degree from nearby Sanderson University only six months ago. Her M.A. is in chemistry, but she double majored in chemistry and biology as an undergraduate while simultaneously getting a minor in physics.

'I love all aspects of science', she said. 'And I'm looking forward to teaching students the things I know'. Ms. Burgess further declared that she prefers a hands-on approach to teaching science. So she expects to conduct numerous experiments in the hope of sparking students' interest in science.

Finally, Ms. Burgess added that she welcomes student participation in her classes. 'Not only can students learn from their teachers, but I believe that teachers can also learn from their students. I hope that, by working together, we can all increase our knowledge of science.'""",
        "content_vi": """Khi học kỳ mùa xuân bắt đầu, học sinh tại Trường Trung học Eastern đã được chào đón bởi một giáo viên khoa học mới. Tên cô ấy là Elaine Burgess, và cô ấy đã thay thế Donald Young, người đã nghỉ hưu để dành thời gian cho các cháu của mình.

Vì cô Burgess mới bắt đầu làm việc ở đây, nhiều học sinh tò mò về lý lịch của cô. Cô đã đủ tốt bụng để ngồi xuống trả lời phỏng vấn với tờ The Quill and Paper. Theo cô Burgess, cô mới nhận bằng thạc sĩ từ Đại học Sanderson gần đó sáu tháng trước. Bằng Thạc sĩ của cô là về hóa học, nhưng cô học song ngành hóa học và sinh học ở bậc đại học trong khi đồng thời học ngành phụ là vật lý.

'Tôi yêu mọi khía cạnh của khoa học', cô nói. 'Và tôi mong muốn được dạy cho học sinh những điều tôi biết'. Cô Burgess tuyên bố thêm rằng cô thích phương pháp thực hành trong giảng dạy khoa học. Vì vậy, cô dự định tiến hành nhiều thí nghiệm với hy vọng khơi dậy sự quan tâm của học sinh đối với khoa học.

Cuối cùng, cô Burgess nói thêm rằng cô hoan nghênh sự tham gia của học sinh trong các lớp học của mình. 'Học sinh không chỉ có thể học từ giáo viên của họ, mà tôi tin rằng giáo viên cũng có thể học từ học sinh của mình. Tôi hy vọng rằng, bằng cách làm việc cùng nhau, tất cả chúng ta đều có thể nâng cao kiến ​​thức khoa học của mình.'""",
        "questions": [
            {"question": "1. Which headline best summarizes the article?", "options": ["A. Science Classes to Features Hands-on Learning", "B. A Chat with the New Science Teacher", "C. The Education of Elaine Burgess", "D. Science Class: Does Anyone Enjoy it?"], "answer": "B. A Chat with the New Science Teacher"},
            {"question": "2. Based on the article, what is probably true about The Quill and Paper?", "options": ["A. It is read by every student.", "B. It is a new textbook.", "C. It was written by Ms. Burgess.", "D. It is the name of a newspaper."], "answer": "D. It is the name of a newspaper."},
            {"question": "3. Which of the following statements does paragraph 2 support?", "options": ["A. This is the second teaching job for Ms. Burgess.", "B. Ms. Burgess has been a teacher for six months.", "C. Ms. Burgess was a professor at Sanderson University.", "D. Ms. Burgess focused on science as an undergraduate."], "answer": "D. Ms. Burgess focused on science as an undergraduate."},
            {"question": "4. What does the author point out by writing about Ms. Burgess's hope of sparking students' interest in science?", "options": ["A. Too many students have little scientific knowledge.", "B. She wants students to be curious about science.", "C. Science is one of the hardest subjects to learn.", "D. Some experiments can be dangerous for students to do."], "answer": "B. She wants students to be curious about science."},
            {"question": "5. What can be inferred from the article about Ms.Burgess?", "options": ["A. Some of her students know more about science than her.", "B. Her grades in graduate school were high.", "C. She expects her students to speak in class.", "D. The subject she knows the least is biology."], "answer": "C. She expects her students to speak in class."}
        ]
    },
    {
        "title": "UNIT 1: Social Trends - We're Living Faster",
        "content": """Not long ago people believed that in the future we would work less, have more free time, and be more relaxed. But sadly this has not happened. Today we work harder, work longer hours, and are more stressed than ten years ago. We walk faster, talk faster, and sleep less than previous generations. And although we are obsessed with machines which save us time, we have less free time than our parents and grandparents had. But what is this doing to our health? An American journalist James Gleick in a new book, Faster: the acceleration of just about everything, says that people who live in cities are suffering from 'hurry sickness' we are always trying to do more things in less time. As a result, our lives are more stressful. He says that if we don't slow down, we won't live as long as our parents. For most people, faster doesn't mean better.

1 No time for the news
Newspaper articles today are shorter and the headlines are bigger. Most people don't have enough time to read the articles, they only read the headlines! On TV and the radio, newsreaders speak more quickly than ten years ago.

2 No time for stories
In the USA there is a book called One-Minute Bedtime Stories for children. These are shorter versions of traditional stories, specially written for 'busy parents' who want to save time!

3 No time to listen
Some answerphones now have 'quick playback' buttons so that we can re-play people's messages faster - we can't waste time listening to people speaking at normal speed.

4 No time to relax
Even when we relax we do everything more quickly. Ten years ago when people went to art galleries they spent ten seconds looking at each picture. Today they spend just three seconds!

5 No time for slow sports
In the USA the national sport, baseball, is not as popular as before it is a slow game and matches take a long time. Nowadays many people prefer faster and more dynamic sports like basketball.

6 ...but more time in our cars
The only thing that is slower than before is the way we drive. Our cars are faster but the traffic is worse so we drive more slowly. We spend more time sitting in our cars, feeling stressed because we are worried that we won't arrive on time. Experts predict that in ten years' time the average speed on the road in cities will be 17 km/h.""",
        "content_vi": """Cách đây không lâu mọi người tin rằng trong tương lai chúng ta sẽ làm việc ít hơn, có nhiều thời gian rảnh hơn và thư giãn hơn. Nhưng đáng buồn là điều này đã không xảy ra. Ngày nay chúng ta làm việc chăm chỉ hơn, làm việc nhiều giờ hơn và căng thẳng hơn mười năm trước. Chúng ta đi bộ nhanh hơn, nói chuyện nhanh hơn và ngủ ít hơn các thế hệ trước. Và mặc dù chúng ta bị ám ảnh bởi những cỗ máy giúp chúng ta tiết kiệm thời gian, chúng ta lại có ít thời gian rảnh hơn cha mẹ và ông bà chúng ta đã có. Nhưng điều này đang làm gì với sức khỏe của chúng ta? Một nhà báo người Mỹ James Gleick trong một cuốn sách mới, 'Faster: the acceleration of just about everything' (Nhanh hơn: sự tăng tốc của hầu hết mọi thứ), nói rằng những người sống ở các thành phố đang mắc phải 'căn bệnh vội vã', chúng ta luôn cố gắng làm nhiều việc hơn trong thời gian ngắn hơn. Do đó, cuộc sống của chúng ta trở nên căng thẳng hơn. Ông nói rằng nếu chúng ta không sống chậm lại, chúng ta sẽ không sống lâu bằng cha mẹ mình. Đối với hầu hết mọi người, nhanh hơn không có nghĩa là tốt hơn.

1 Không có thời gian cho tin tức
Các bài báo ngày nay ngắn hơn và tiêu đề lớn hơn. Hầu hết mọi người không có đủ thời gian để đọc các bài báo, họ chỉ đọc tiêu đề! Trên TV và đài phát thanh, những người đọc tin tức nói nhanh hơn so với mười năm trước.

2 Không có thời gian cho những câu chuyện
Ở Mỹ có một cuốn sách tên là Chuyện kể trước khi đi ngủ trong một phút dành cho trẻ em. Đây là những phiên bản ngắn hơn của các câu chuyện truyền thống, được viết đặc biệt cho 'những bậc cha mẹ bận rộn', những người muốn tiết kiệm thời gian!

3 Không có thời gian để lắng nghe
Một số máy trả lời tự động hiện có nút 'phát lại nhanh' để chúng ta có thể nghe lại tin nhắn của mọi người nhanh hơn - chúng ta không thể lãng phí thời gian để nghe mọi người nói ở tốc độ bình thường.

4 Không có thời gian để thư giãn
Ngay cả khi thư giãn, chúng ta cũng làm mọi thứ nhanh hơn. Mười năm trước khi mọi người đến các phòng trưng bày nghệ thuật, họ dành mười giây để nhìn vào mỗi bức tranh. Ngày nay họ chỉ dành ba giây!

5 Không có thời gian cho các môn thể thao chậm
Ở Mỹ, môn thể thao quốc gia, bóng chày, không còn phổ biến như trước, đó là một trò chơi chậm và các trận đấu diễn ra trong một thời gian dài. Ngày nay nhiều người thích các môn thể thao nhanh hơn và năng động hơn như bóng rổ.

6 ...nhưng có nhiều thời gian hơn trong ô tô của chúng ta
Điều duy nhất chậm hơn trước đây là cách chúng ta lái xe. Ô tô của chúng ta nhanh hơn nhưng giao thông lại tệ hơn nên chúng ta lái xe chậm hơn. Chúng ta dành nhiều thời gian hơn ngồi trong xe, cảm thấy căng thẳng vì lo lắng rằng chúng ta sẽ không đến đúng giờ. Các chuyên gia dự đoán rằng trong mười năm tới, tốc độ trung bình trên đường ở các thành phố sẽ là 17 km/h.""",
        "questions": [
            {"question": "1. What is the main idea of this paragraph: North Americans send cards for many occasions. They send cards to family and friends on birthdays and holidays. They also send thank-you cards, get well cards, graduation cards, and congratulation cards...", "options": ["A. Sending cards is very popular in North America.", "B. Birthday cards are the most popular kind of card.", "C. It is important to send thank-you cards."], "answer": "A. Sending cards is very popular in North America."},
            {"question": "2. What is the main idea of this paragraph: First of all, we need money to repair old roads and build new roads. We also need more to pay teachers' salaries and to pay for services such as trash collection...", "options": ["A. We should raise city taxes.", "B. City taxes are too high.", "C. City taxes pay for new roads."], "answer": "A. We should raise city taxes."},
            {"question": "3. What is the main idea of this paragraph: One thing you must consider is the quality of the university's educational program. You also need to think about the school's size and location...", "options": ["A. It is expensive to attend a university in the United States.", "B. There are several factors to consider when you choose a university to attend.", "C. You should consider getting a good education."], "answer": "B. There are several factors to consider when you choose a university to attend."},
            {"question": "4. What is the main idea of this paragraph: For example, a person can have breakfast in New York, board an airplane, and have dinner in Paris. A businesswoman in London can instantly place an order with a factory in Hong Kong by sending a fax...", "options": ["A. Airplanes have changed our lives.", "B. Advances in technology have made the world seem smaller.", "C. The fax machine was an important invention."], "answer": "B. Advances in technology have made the world seem smaller."}
        ]
    },
    {
        "title": "UNIT 2: The World of Colours",
        "content": """Clothes are like a second skin. Most likely you feel good when you wear your favorite color. What happens when someone sees you wearing any color for example blue? Does the color send a message?

One of the most common examples of color symbolism in clothing is the custom of using pink for girls and blue for boys, but it wasn't always this way. This tradition emerged at the turn of the 20th century. Since pink was thought to be a stronger color, it was best suited for boys; blue was more delicate and dainty and best for girls. In 1921, the Women's Institute for Domestic Science in Pennsylvania endorsed pink for boys, blue for girls.

Even more interesting is the fact that pink is the color for baby boys and blue is the color for baby girls in Belgium today. Another interesting fact about pink is that pink is a very masculine color in Bermuda. Also, British bankers and barristers have worn pink shirts for decades. Pink goes in and out of fashion in other parts of the world. White is the traditional color for a bride's wedding gown in the U.S. and most European cultures. White symbolizes purity and innocence.

What about the color worn for weddings and funerals?
In Asia, white is the color of death. This arises from the belief that death is seen as a beginning and that white represents the purity that the deceased brings into the next life. Therefore, brides in Japan and China wear red in traditional wedding ceremonies. White is also associated with death in India, where widows wear white. Consequently, red or pink saris are the most popular colors for brides.

What about black clothes?
Black symbolizes death and is the traditional color of mourning in Western cultures. Black clothing is associated with powerful forces in many parts of the world. Bad and good Witches, the devil, ninjas, cat burglars, Darth Vader, Cat Woman, and Batman wear black....and so do priests, nuns, judges, mimes, Mennonites, Bedouins, and monks. Maybe the common thread is that these people are signaling their seriousness of purpose or the need to be hard to see - or both.""",
        "content_vi": """Quần áo giống như làn da thứ hai. Hầu hết có khả năng bạn cảm thấy tốt khi bạn mặc màu sắc yêu thích của bạn. Điều gì xảy ra khi ai đó nhìn thấy bạn mặc bất kỳ màu nào ví dụ như màu xanh lam? Màu sắc có gửi một thông điệp không?

Một trong những ví dụ phổ biến nhất về tính biểu tượng của màu sắc trong quần áo là phong tục sử dụng màu hồng cho bé gái và màu xanh lam cho bé trai, nhưng không phải lúc nào cũng như vậy. Truyền thống này xuất hiện vào đầu thế kỷ 20. Vì màu hồng được cho là màu mạnh mẽ hơn, nên nó phù hợp nhất với các bé trai; màu xanh lam tinh tế và nhã nhặn hơn và tốt nhất cho các bé gái. Năm 1921, Viện Khoa học Trong nước dành cho Phụ nữ ở Pennsylvania đã chứng thực màu hồng cho bé trai, màu xanh lam cho bé gái.

Thú vị hơn nữa là thực tế màu hồng là màu của bé trai và màu xanh lam là màu của bé gái ở Bỉ ngày nay. Một sự thật thú vị khác về màu hồng là màu hồng là một màu rất nam tính ở Bermuda. Ngoài ra, các chủ ngân hàng và luật sư người Anh đã mặc áo sơ mi màu hồng trong nhiều thập kỷ. Màu hồng lúc thì thịnh hành lúc thì lỗi mốt ở các nơi khác trên thế giới. Màu trắng là màu truyền thống cho váy cưới của cô dâu ở Hoa Kỳ và hầu hết các nền văn hóa châu Âu. Màu trắng tượng trưng cho sự thuần khiết và vô tội.

Thế còn màu sắc trang phục cho đám cưới và đám tang thì sao?
Ở châu Á, màu trắng là màu của cái chết. Điều này phát sinh từ niềm tin rằng cái chết được coi là một sự khởi đầu và màu trắng đại diện cho sự thuần khiết mà người chết mang vào kiếp sau. Do đó, các cô dâu ở Nhật Bản và Trung Quốc mặc màu đỏ trong các nghi lễ cưới truyền thống. Màu trắng cũng gắn liền với cái chết ở Ấn Độ, nơi các góa phụ mặc đồ trắng. Do đó, saris màu đỏ hoặc màu hồng là màu phổ biến nhất cho các cô dâu.

Quần áo màu đen thì sao?
Màu đen tượng trưng cho cái chết và là màu tang tóc truyền thống trong các nền văn hóa phương Tây. Quần áo màu đen gắn liền với các thế lực hùng mạnh ở nhiều nơi trên thế giới. Phù thủy tốt và xấu, ác quỷ, ninja, những tên trộm cắp, Darth Vader, Cat Woman và Batman mặc đồ đen....và các linh mục, nữ tu, thẩm phán, nghệ sĩ kịch câm, người Mennonite, người Bedouin và các nhà sư cũng vậy. Có lẽ điểm chung là những người này đang ra hiệu về sự nghiêm túc trong mục đích của họ hoặc nhu cầu khó bị nhìn thấy - hoặc cả hai.""",
        "questions": [
            {"question": "1. In the 20th century, which color was originally thought to be best suited for boys because it was a stronger color?", "options": ["A. Pink", "B. Blue", "C. White", "D. Black"], "answer": "A. Pink"},
            {"question": "2. In Belgium today, pink is the color for:", "options": ["A. Baby girls", "B. Baby boys", "C. Brides", "D. Widows"], "answer": "B. Baby boys"},
            {"question": "3. In Asia, what is white often considered the color of?", "options": ["A. Marriage", "B. Power", "C. Death", "D. Birth"], "answer": "C. Death"},
            {"question": "4. What color do brides in Japan and China traditionally wear?", "options": ["A. White", "B. Black", "C. Blue", "D. Red"], "answer": "D. Red"}
        ]
    },
    {
        "title": "UNIT 3: Politeness - Etiquette",
        "content": """Text 1: Bad manners at work
Etiquette is the name we give to the rules for being polite in a social group. Business etiquette is important for people who often have to make new contacts and build relationships in their work. Politeness can also help to improve the working environment for people in the same office. Some cultures and situations are formal, which means that we have to follow rules; other cultures and situations are more informal.

Text 2: Office workers "admit being rude"
Most office workers say they are rude or bad-mannered at work. Two out of three workers regularly arrive late for meetings, most ignore emails and three out of four use bad language. In a survey of 1,000 workers, two-thirds say that pressure of work is the reason for bad manners.

Other common examples of bad office etiquette include ignoring colleagues and answering mobile phone calls during meetings. Using mobile phones in meetings is impolite and distracts others, research by the University of Surrey shows. If you respond to call when speaking to somebody, it means that the phone call is more important than the person, the survey said. If you answer a call during a meeting, it could mean that the meeting is not important.

Mr Jacobs, managing director of Office Angels, a recruitment firm say it is easy for people to forget their manners in the working environment, which is often very informal and very busy. Workers can forget proper etiquette such as introducing people at meetings, and this is often bad for working relationships.

Psychologist Dr Colin Gill believes that people are not as polite as they were twenty years ago. He said: 'Courtesy is no longer something that is so much respected in our society. People think it is 'stuffy to be polite or formal.'

Now some organisations are actually investing money in training their junior managers to be polite. Office Angels is encouraging people to arrive on time for meetings, turn off mobile phones and avoid bad manners at work is such a simple thing to do, Mr Jacobs says, 'and it can have a dramatic impact on improving your working environment and your relationships with others.' """,
        "content_vi": """Văn bản 1: Cư xử tệ tại nơi làm việc
Phép xã giao (Etiquette) là tên chúng ta gọi các quy tắc để lịch sự trong một nhóm xã hội. Phép xã giao trong kinh doanh rất quan trọng đối với những người thường xuyên phải tạo các mối liên hệ mới và xây dựng các mối quan hệ trong công việc của họ. Lịch sự cũng có thể giúp cải thiện môi trường làm việc cho những người trong cùng một văn phòng. Một số nền văn hóa và tình huống mang tính hình thức, có nghĩa là chúng ta phải tuân theo các quy tắc; các nền văn hóa và tình huống khác thì thân mật hơn.

Văn bản 2: Nhân viên văn phòng 'thừa nhận thô lỗ'
Hầu hết các nhân viên văn phòng nói rằng họ thô lỗ hoặc cư xử không tốt tại nơi làm việc. Cứ ba nhân viên thì có hai người thường xuyên đến muộn trong các cuộc họp, hầu hết phớt lờ email và ba trong bốn người sử dụng ngôn ngữ không tốt. Trong một cuộc khảo sát với 1.000 công nhân, hai phần ba nói rằng áp lực công việc là lý do của cách cư xử không tốt.

Các ví dụ phổ biến khác về phép xã giao tồi tệ ở văn phòng bao gồm phớt lờ đồng nghiệp và trả lời điện thoại di động trong các cuộc họp. Việc sử dụng điện thoại di động trong các cuộc họp là bất lịch sự và làm người khác mất tập trung, nghiên cứu của Đại học Surrey cho thấy. Khảo sát cho biết, nếu bạn trả lời cuộc gọi khi đang nói chuyện với ai đó, điều đó có nghĩa là cuộc gọi điện thoại quan trọng hơn người đó. Nếu bạn trả lời một cuộc gọi trong một cuộc họp, nó có thể có nghĩa là cuộc họp đó không quan trọng.

Ông Jacobs, giám đốc điều hành của Office Angels, một công ty tuyển dụng nói rằng mọi người rất dễ quên cách cư xử của mình trong môi trường làm việc, vốn thường rất thân mật và rất bận rộn. Người lao động có thể quên các phép xã giao đúng mực chẳng hạn như giới thiệu mọi người tại các cuộc họp, và điều này thường tồi tệ cho các mối quan hệ công việc.

Nhà tâm lý học, Tiến sĩ Colin Gill tin rằng mọi người không còn lịch sự như họ của hai mươi năm trước. Ông nói: 'Sự lịch sự không còn là thứ được tôn trọng nhiều trong xã hội của chúng ta nữa. Mọi người nghĩ rằng lịch sự hay trang trọng là 'cứng nhắc'.' 

Giờ đây, một số tổ chức thực sự đang đầu tư tiền vào việc đào tạo các nhà quản lý cấp dưới của họ trở nên lịch sự. Office Angels đang khuyến khích mọi người đến đúng giờ trong các cuộc họp, tắt điện thoại di động và tránh cư xử không tốt tại nơi làm việc là một việc đơn giản để làm, ông Jacobs nói, 'và nó có thể có tác động đáng kể đến việc cải thiện môi trường làm việc và các mối quan hệ của bạn với người khác.'""",
        "questions": [
            {"question": "1. The aim of the texts is to", "options": ["A. reflect the fact of officer's good manners at work with illustrations", "B. reflect the fact of officer's bad manners at work with illustrations", "C. encourage officer's bad manners at work"], "answer": "B. reflect the fact of officer's bad manners at work with illustrations"},
            {"question": "2. In paragraph 2, the author wants to", "options": ["A. give specific examples of bad manners at work", "B. give advice on how to behave politely at work", "C. give specific figures of bad manners at work"], "answer": "A. give specific examples of bad manners at work"},
            {"question": "3. The purpose of some organisations who invest money in training their junior managers to be polite is to", "options": ["A. improve the working environment and relationships with others", "B. help them more famous", "C. spend all money they have"], "answer": "A. improve the working environment and relationships with others"}
        ]
    },
    {
        "title": "UNIT 4: Games - The Olympic Games",
        "content": """During the Olympic Games, people from all over the world come together in the peace and friendship. Some of these people compete for medals. Several million people attend the games, and millions of other people watch them on television.
Why do we have the Olympic Games? How did they begin? The first Olympic Games that we have records of were in Greece in 776 B.C. The games lasted one day. The only event in the first Olympic Games was a race. Men ran the length or the stadium (about 192 meters). Then, longer running races were added. Through the years, a few other kinds of events, like the long jump, were also added. During this time, the games were for men only, and women could not even watch them. In the year 393, a Roman emperor ended the Olympic Game because the quality of the games became very low. The Olympics did not take place again for 1500 years!

In 1984, Pierre de Coubertin of France helped form the International Olympic Committee, and the modern Olympic Games began. In1896, the games were held again in Athens, Greece. The Greeks built a new stadium for the competition. Three hundred and eleven athletes from thirteen countries competed in many events. The winners became national heroes.

After 1896, the games were held every four years during the summer in different cities around the world. In 1900, the Olympics were in Paris, France, and women competed for the first time. In 1908, in London, England, the first gold medals were given to winning athletes. Before that time, the winners received only silver and bronze medals. The Olympic flag was first introduced in 1920 in Antwerp, Belgium. The flag has five rings on it. The rings represent the continents of Africa, Asia, Australia, Europe, and North and South American. Each ring is a different color blue, yellow, black, green, or red because the flag of each of the countries that compete in the games has at least one of these colors in it.

The Olympic Winter games began in 1924 in Chamonix, France. Athletes competed in winter events such as skiing, ice skating, and ice hockey. Today, the Winter Games take places every four years. The Summer Games also take place every four years, but not in the same year as the winter events. Both the Summer Games and the Winter Games must have at least fifteen events, and they cannot last more than sixteen days.

Until recently, Olympic competitors could not be professional athletes. All of the athletes in the Olympic Games were amateurs. Today, however, many of the Olympic athletes are professional who play their sports for money during the year. Some people disagree with this idea. They believe that the Olympic game are for amateur athletes, not paid professionals. Other people think that any one can play in the Olympic Games.""",
        "content_vi": """Trong Thế vận hội Olympic, mọi người từ khắp nơi trên thế giới đến với nhau trong hòa bình và tình bạn. Một số người trong số họ thi đấu để giành huy chương. Vài triệu người tham dự các trò chơi, và hàng triệu người khác xem chúng trên truyền hình.
Tại sao chúng ta có Thế vận hội Olympic? Chúng bắt đầu như thế nào? Thế vận hội Olympic đầu tiên mà chúng ta có ghi chép lại là ở Hy Lạp vào năm 776 trước Công nguyên. Thế vận hội kéo dài một ngày. Sự kiện duy nhất trong Thế vận hội Olympic đầu tiên là một cuộc đua. Những người đàn ông chạy dọc theo chiều dài của sân vận động (khoảng 192 mét). Sau đó, các cuộc đua chạy dài hơn đã được thêm vào. Qua nhiều năm, một vài loại sự kiện khác, như nhảy xa, cũng được thêm vào. Trong thời gian này, các trò chơi chỉ dành cho nam giới, và phụ nữ thậm chí không thể xem chúng. Vào năm 393, một hoàng đế La Mã đã chấm dứt Thế vận hội Olympic vì chất lượng của các trò chơi trở nên rất thấp. Thế vận hội đã không diễn ra một lần nữa trong 1500 năm!

Vào năm 1984, Pierre de Coubertin của Pháp đã giúp thành lập Ủy ban Olympic Quốc tế, và Thế vận hội Olympic hiện đại bắt đầu. Năm 1896, thế vận hội lại được tổ chức tại Athens, Hy Lạp. Người Hy Lạp đã xây dựng một sân vận động mới cho cuộc thi. Ba trăm mười một vận động viên từ mười ba quốc gia đã tranh tài trong nhiều sự kiện. Những người chiến thắng đã trở thành anh hùng dân tộc.

Sau năm 1896, các trò chơi được tổ chức bốn năm một lần trong mùa hè ở các thành phố khác nhau trên thế giới. Vào năm 1900, Thế vận hội diễn ra ở Paris, Pháp, và phụ nữ lần đầu tiên thi đấu. Vào năm 1908, tại London, Anh, những chiếc huy chương vàng đầu tiên đã được trao cho các vận động viên chiến thắng. Trước thời gian đó, những người chiến thắng chỉ nhận được huy chương bạc và đồng. Cờ Olympic lần đầu tiên được giới thiệu vào năm 1920 tại Antwerp, Bỉ. Lá cờ có năm vòng tròn trên đó. Các vòng đại diện cho các lục địa Châu Phi, Châu Á, Châu Úc, Châu Âu, và Bắc và Nam Mỹ. Mỗi vòng là một màu khác nhau - xanh dương, vàng, đen, xanh lá cây hoặc đỏ vì quốc kỳ của mỗi quốc gia tham gia thi đấu tại các trò chơi có ít nhất một trong những màu này trong đó.

Thế vận hội Mùa đông bắt đầu vào năm 1924 tại Chamonix, Pháp. Các vận động viên thi đấu trong các sự kiện mùa đông như trượt tuyết, trượt băng và khúc côn cầu trên băng. Ngày nay, Thế vận hội Mùa đông diễn ra bốn năm một lần. Thế vận hội Mùa hè cũng diễn ra bốn năm một lần, nhưng không cùng năm với các sự kiện mùa đông. Cả Thế vận hội Mùa hè và Thế vận hội Mùa đông phải có ít nhất mười lăm sự kiện, và chúng không thể kéo dài quá mười sáu ngày.

Cho đến gần đây, những người tham gia thi đấu Olympic không thể là những vận động viên chuyên nghiệp. Tất cả các vận động viên trong Thế vận hội Olympic đều là nghiệp dư. Tuy nhiên, ngày nay, nhiều vận động viên Olympic là những người chuyên nghiệp chơi thể thao của họ vì tiền trong năm. Một số người không đồng ý với ý tưởng này. Họ tin rằng Thế vận hội Olympic là dành cho các vận động viên nghiệp dư, không phải là những chuyên gia được trả lương. Những người khác nghĩ rằng bất cứ ai cũng có thể chơi trong Thế vận hội Olympic.""",
        "questions": [
            {"question": "1. True or False: The first Olympic competitors ran the length of the stadium.", "options": ["A. True", "B. False"], "answer": "A. True"},
            {"question": "2. True or False: Pierre de Coubertin was an athlete in the first modern games.", "options": ["A. True", "B. False"], "answer": "B. False"},
            {"question": "3. True or False: Winners have always received gold medals.", "options": ["A. True", "B. False"], "answer": "B. False"},
            {"question": "4. True or False: The Olympic flag has six colored rings on it.", "options": ["A. True", "B. False"], "answer": "B. False"},
            {"question": "5. True or False: The summer and winter games take place in the same year.", "options": ["A. True", "B. False"], "answer": "B. False"},
            {"question": "6. True or False: Today both men and women compete in the Olympics.", "options": ["A. True", "B. False"], "answer": "A. True"}
        ]
    },
    {
        "title": "UNIT 5: Family Life - The Royal Family",
        "content": """1. Prince William is a member of the British royal family. He's the Queen's grandson and the eldest son of Charles and Diana. His brother's name is Harry. Diana, their mother, isn't alive now, but they have a stepmother, Camilla.

2. William's wife is Kate Middleton. She's originally from an ordinary family- but of course, she's now the Duchess of Cambridge and part of the royal family! Kate has a brother, James, and a sister, Pippa. Their parents, Michael and Carole, have an online business.

3. In some ways, Kate and William are a normal couple. They have friends from university and they have hobbies and interests too. For example, William loves football and Kate likes photography. In the winter, they go skiing together.

4. In other ways, their lives are very different from their friends' lives. William is the future King of the United Kingdom and fifteen other countries too, including Canada and Australia. Kate and William have a lot of official duties. They help charities in the UK and Africa, they visit other countries and they meet important visitors to the UK.

5. The Duchess of Cambridge is expecting a baby, St James's Palace has confirmed. All the Members of the Royal Family and the duchess's family, the Middletons, are delighted: "The Queen, the Duke of Edinburgh, the Prince of Wales, the Duchess of Cornwall and Prince Harry and members of both families are delighted with the news."
The baby will be third in line to the throne, after Prince Charles and Prince William. A spokesman said the duchess has been admitted to King Edward VII Hospital in central London with acute morning sickness and is expected to stay for several days.

6. Prince William, the Duke of Cambridge, says he and his wife "could not be happier" after the duchess gave birth to a baby boy, at 16:30, 22nd July 2013 UK time at St Mary's Hospital, west London. William was present at St Mary's for the birth. The young parents spent time with their son before telling the news to their families and the world. The Queen's gynecologist Marcus Setchell, who led the team that delivered the baby, described the new arrival as "wonderful baby, beautiful baby". A bulletin signed by him was taken by a royal aide from St Mary's to the palace under police escort. The news has been since displayed on an easel in the forecourt of Buckingham Palace in line with tradition. A Palace spokesman said the names of the baby would be announced in due course. A Buckingham Palace spokesman said: "The Queen and Duke of Edinburgh are delighted at the news." """,
        "content_vi": """1. Hoàng tử William là một thành viên của gia đình hoàng gia Anh. Anh là cháu trai của Nữ hoàng và là con trai cả của Charles và Diana. Tên của em trai anh ấy là Harry. Diana, mẹ của họ, hiện không còn sống, nhưng họ có một người mẹ kế, Camilla.

2. Vợ của William là Kate Middleton. Ban đầu cô ấy xuất thân từ một gia đình bình thường- nhưng tất nhiên, hiện giờ cô ấy là Nữ công tước xứ Cambridge và là một phần của gia đình hoàng gia! Kate có một người anh trai, James, và một người em gái, Pippa. Cha mẹ của họ, Michael và Carole, có một doanh nghiệp trực tuyến.

3. Về một số mặt, Kate và William là một cặp đôi bình thường. Họ có những người bạn từ thời đại học và họ cũng có những sở thích và đam mê. Ví dụ, William yêu thích bóng đá và Kate thích nhiếp ảnh. Vào mùa đông, họ cùng nhau đi trượt tuyết.

4. Ở một khía cạnh khác, cuộc sống của họ rất khác so với cuộc sống của bạn bè họ. William là vị Vua tương lai của Vương quốc Anh và mười lăm quốc gia khác nữa, bao gồm cả Canada và Úc. Kate và William có rất nhiều nhiệm vụ chính thức. Họ giúp đỡ các tổ chức từ thiện ở Vương quốc Anh và Châu Phi, họ đến thăm các quốc gia khác và họ gặp gỡ những vị khách quan trọng đến Vương quốc Anh.

5. Cung điện St James đã xác nhận rằng Nữ công tước xứ Cambridge đang mong đợi một em bé. Tất cả các Thành viên của Gia đình Hoàng gia và gia đình của nữ công tước, gia đình Middleton, đều vui mừng: 'Nữ hoàng, Công tước xứ Edinburgh, Thân vương xứ Wales, Nữ công tước xứ Cornwall và Hoàng tử Harry cùng các thành viên của cả hai gia đình đều vui mừng trước tin này.'
Đứa bé sẽ đứng thứ ba trong danh sách kế vị ngai vàng, sau Thái tử Charles và Hoàng tử William. Một phát ngôn viên cho biết nữ công tước đã được đưa vào Bệnh viện King Edward VII ở trung tâm London với chứng ốm nghén cấp tính và dự kiến sẽ ở lại trong vài ngày.

6. Hoàng tử William, Công tước xứ Cambridge, nói rằng anh và vợ 'không thể hạnh phúc hơn' sau khi nữ công tước hạ sinh một bé trai, lúc 16:30, ngày 22 tháng 7 năm 2013 theo giờ Vương quốc Anh tại Bệnh viện St Mary, tây London. William đã có mặt tại St Mary khi sinh. Đôi cha mẹ trẻ đã dành thời gian cho con trai mình trước khi thông báo tin tức cho gia đình và thế giới. Bác sĩ phụ khoa của Nữ hoàng, Marcus Setchell, người dẫn đầu đội ngũ đỡ đẻ cho em bé, đã mô tả sinh linh mới chào đời là 'em bé tuyệt vời, em bé xinh đẹp'. Một bản thông báo có chữ ký của ông đã được một phụ tá hoàng gia đưa từ St Mary đến cung điện dưới sự hộ tống của cảnh sát. Tin tức này đã được hiển thị trên một giá vẽ ở sân trước của Cung điện Buckingham theo đúng truyền thống. Một phát ngôn viên của Cung điện cho biết tên của em bé sẽ được công bố vào thời điểm thích hợp. Một phát ngôn viên của Cung điện Buckingham cho biết: 'Nữ hoàng và Công tước xứ Edinburgh rất vui mừng trước tin tức này.'""",
        "questions": [
            {"question": "1. True or False: Camilla is William's mother.", "options": ["A. True", "B. False"], "answer": "B. False"},
            {"question": "2. True or False: William's wife is the Duchess of Cambridge.", "options": ["A. True", "B. False"], "answer": "A. True"},
            {"question": "3. True or False: Kate is one of two children.", "options": ["A. True", "B. False"], "answer": "B. False"},
            {"question": "4. True or False: James is William's cousin.", "options": ["A. True", "B. False"], "answer": "B. False"},
            {"question": "5. True or False: William is a football fan.", "options": ["A. True", "B. False"], "answer": "A. True"},
            {"question": "6. True or False: The King or Queen of England is also the King or Queen of Australia.", "options": ["A. True", "B. False"], "answer": "A. True"},
            {"question": "7. True or False: William was absent from St Mary's for the birth.", "options": ["A. True", "B. False"], "answer": "B. False"}
        ]
    }
]

def main():
    st.set_page_config(page_title="English Self-Study App (Offline)", layout="wide")
    st.title("📚 English Reading Comprehension Practice")
    st.markdown("Chế độ Offline 100%: Tích hợp toàn bộ bản dịch Tiếng Việt.")
    
    st.sidebar.header("Chọn bài đọc")
    
    passage_titles = [d["title"] for d in data]
    selected_passage = st.sidebar.selectbox("Danh sách bài đọc", passage_titles)
    
    passage_data = next(d for d in data if d["title"] == selected_passage)
    
    st.subheader(passage_data["title"])
    st.write(passage_data["content"])

    # Chức năng dịch Offline 
    if st.toggle("🌐 Xem bản dịch Tiếng Việt (Offline)"):
        if "content_vi" in passage_data and passage_data["content_vi"].strip() != "":
            st.info(passage_data["content_vi"])
        else:
            st.warning("⚠️ Bài đọc này chưa được cập nhật bản dịch tiếng Việt offline.")
    
    st.divider()
    st.subheader("Questions")
    
    user_answers = {}
    for i, q in enumerate(passage_data["questions"]):
        user_answers[i] = st.radio(f"**{q['question']}**", q["options"], index=None, key=f"q_{i}")
        
    if st.button("Submit Answers", type="primary"):
        score = 0
        st.subheader("Results")
        for i, q in enumerate(passage_data["questions"]):
            if user_answers[i] == q["answer"]:
                st.success(f"{q['question']}: Correct! ({q['answer']})")
                score += 1
            else:
                st.error(f"{q['question']}: Incorrect. The correct answer is {q['answer']}")
        st.info(f"Your Score: {score} / {len(passage_data['questions'])}")

if __name__ == '__main__':
    main()
