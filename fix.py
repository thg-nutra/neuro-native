import re

with open('pressel/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The original article content starts after <main class="article-content">
# and ends before </main> or before the facebook comments section.

new_article_content = """
    <div class="media-card">
      <a href="/neuro-vid" target="_blank">
        <img src="/images/01.png" alt="Tom Hanks Interview">
      </a>
    </div>

    <p>The world watched in tears as <strong>Tom Hanks</strong> — America's most beloved actor — broke down crying in a recent interview about his battle with <strong>diabetic neuropathy.</strong></p>

    <p>"I was so angry," Tom revealed. "I spent years feeling my feet go numb, the burning, the tingling keeping me up at night."</p>

    <p>"Doctors told me I might lose my foot to <strong>amputation.</strong> And the answer was sitting in my kitchen cabinet the whole time."</p>

    <p>So, if you're suffering from <strong>neuropathy</strong> — the nerve pain, the numbness, that horrible 'pins and needles' feeling in your hands and feet...</p>

    <h4 style="color: #ff0000; font-weight: 700;">You're NOT alone.</h4>

    <p>After his diagnosis, Tom reached out to <strong>Dr. Oz</strong> — the Harvard-trained physician who became America's most trusted doctor and has been called "the most influential voice in medicine" by TIME Magazine.</p>

    <p>What Dr. Oz discovered about the REAL cause of Tom's neuropathy <strong>changed everything</strong> — and it's now helping thousands of Americans save their feet from amputation.</p>

    <p>The impact was so great that Dr. Oz was invited for an exclusive interview on <strong>60 Minutes</strong> with Sharyn Alfonsi, where he shared the step-by-step protocol Tom's family is now using.</p>

    <div class="media-card">
      <a href="/neuro-vid" target="_blank">
        <img src="/images/02.png" alt="Dr Oz and Sharyn">
      </a>
    </div>

    <h2 style="text-align: center; font-weight: 700; margin-top: 30px; margin-bottom: 20px;">During the interview, Dr. Oz <strong style="color: #ff0000;">shocked</strong> the audience by stating:</h2>

    <div class="media-card">
      <a href="/neuro-vid" target="_blank">
        <img src="/images/03.png" alt="Shocked Audience">
      </a>
    </div>

    <p><strong>Sharyn:</strong> Dr. Oz, millions watched Tom Hanks interview in tears. What did you tell him that changed everything?</p>

    <div class="media-card">
      <a href="/neuro-vid" target="_blank">
        <img src="/images/04.png" alt="Dr Oz Explaining">
      </a>
    </div>

    <p><strong>Dr. Oz:</strong> The truth that <strong>only 0.3%</strong> of doctors know: neuropathy isn't just diabetes or age — it's <strong>microplastics</strong> poisoning your nerves.</p>

    <p>Tiny plastic particles hidden in <strong>your food, water, and even the air you breathe.</strong> They've been building up in your body for 40, 50 years.</p>

    <p>And they settle in your hands and feet — <strong>exactly where neuropathy strikes.</strong></p>

    <p>They block the electrical signals between your nerves, like static on a phone line. That's what causes the burning, the tingling, the numbness.</p>

    <p>Tom had been exposed to them his whole life without knowing. When I explained this, he broke down crying.</p>

    <div class="media-card">
      <a href="/neuro-vid" target="_blank">
        <img src="/images/05.png" alt="Microplastics effect">
      </a>
    </div>

    <p><strong>Sharyn:</strong> Your 'Pink Salt Trick' segment got over <strong>4.5 million views</strong>. Is that what you gave Tom?</p>

    <div class="media-card">
      <a href="/neuro-vid" target="_blank">
        <img src="/images/06.png" alt="Pink Salt Trick">
      </a>
    </div>

    <p><strong>Dr. Oz:</strong> Exactly. One teaspoon of pink Himalayan salt combined with a common yellow spice — it binds to those microplastics, flushes them right out through your urine, and lets your nerves finally heal.</p>

    <p>Tom told me the burning in his feet stopped after just 10 days. First time in years he slept through the night. His doctors couldn't believe it — they had already scheduled him for amputation.</p>

    <p>He canceled it. The family was in tears — happy tears this time.</p>

    <div class="media-card">
      <a href="/neuro-vid" target="_blank">
        <img src="/images/07.png" alt="Tom Hanks Smiling">
      </a>
    </div>

    <p><strong>Sharyn:</strong> Can anyone try this at home?</p>

    <div class="media-card">
      <a href="/neuro-vid" target="_blank">
        <img src="/images/09.png" alt="Ingredients">
      </a>
    </div>

    <p><strong>Dr. Oz:</strong> You probably have this ingredient in your kitchen right now.</p>

    <p>Most people feel the difference <strong>in just 3-5 days</strong> — the tingling fades, the burning stops, that feeling in your feet you thought was gone forever starts coming back.</p>

    <p>I'm 64 and I use this every morning. It's my secret weapon for keeping my nerves healthy.</p>

    <p>I made a short video explaining exactly how to do this at home — the exact type of pink salt, what the yellow spice is, the precise amount, and when to take it.</p>

    <h2 style="text-align: center; font-weight: 700; margin-top: 40px; margin-bottom: 20px;">WATCH THE 5-MINUTE VIDEO TO REVERSE NEUROPATHY FOR GOOD</h2>

    <div class="media-card">
      <a href="/neuro-vid" target="_blank">
        <img src="/images/09.png" alt="Play Video">
      </a>
    </div>

    <div class="cta-btn-wrapper">
      <a class="cta-button" href="/neuro-vid" target="_blank">CLICK TO WATCH</a>
    </div>

    <h1 style="color: #ff0000; text-align: center; margin: 40px 0;">See Other Celebrities Who Also Canceled Their Amputation</h1>

    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
        <div style="display: flex; gap: 15px; align-items: center; margin-bottom: 15px;">
            <img src="/images/01.jpg" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; border: 2px solid white; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" alt="Patti LaBelle">
            <div>
                <div style="color: #ffc107; font-size: 14px; margin-bottom: 5px;">★★★★★</div>
                <h3 style="margin: 0; font-size: 18px; font-weight: 700;">Patti LaBelle</h3>
            </div>
        </div>
        <p style="margin: 0; font-size: 16px; color: #555;">For years, my feet were numb and constantly tingling. Doctors kept giving me pills, but nothing fixed the problem. Then I discovered Dr. Oz’s Pink Salt Ritual. After a few weeks, the burning started to calm down and I could finally walk without that constant discomfort.</p>
    </div>

    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
        <div style="display: flex; gap: 15px; align-items: center; margin-bottom: 15px;">
            <img src="/images/02.jpg" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; border: 2px solid white; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" alt="Halle Berry">
            <div>
                <div style="color: #ffc107; font-size: 14px; margin-bottom: 5px;">★★★★★</div>
                <h3 style="margin: 0; font-size: 18px; font-weight: 700;">Halle Berry</h3>
            </div>
        </div>
        <p style="margin: 0; font-size: 16px; color: #555;">This simple nerve ritual is incredible. In just a few weeks, the burning and tingling in my feet started to fade. And within a couple of months, the numbness was almost completely gone. And no, it wasn’t medication or injections like most people assume. It was all thanks to this simple daily routine I started every morning. The test results you see here are the real results of this natural method, just like Dr. Oz explained to me. I truly believe anyone struggling with neuropathy should try this. Because it really works — and you can feel the difference in just days.</p>
    </div>

    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; margin-bottom: 20px;">
        <div style="display: flex; gap: 15px; align-items: center; margin-bottom: 15px;">
            <img src="/images/03.webp" style="width: 60px; height: 60px; border-radius: 50%; object-fit: cover; border: 2px solid white; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" alt="Randy Jackson">
            <div>
                <div style="color: #ffc107; font-size: 14px; margin-bottom: 5px;">★★★★★</div>
                <h3 style="margin: 0; font-size: 18px; font-weight: 700;">Randy Jackson</h3>
            </div>
        </div>
        <p style="margin: 0; font-size: 16px; color: #555;">I struggled with neuropathy for years — burning feet, numb toes, constant tingling. But the Pink Salt Trick I heard about from Dr. Oz changed everything. In just days, the burning started to fade and the tingling calmed down in a way nothing else ever did.</p>
    </div>

    <h2 style="text-align: center; font-weight: 700; margin-top: 40px; margin-bottom: 20px;">WATCH THE 5-MINUTE VIDEO TO REVERSE NEUROPATHY FOR GOOD</h2>

    <div class="media-card">
      <a href="/neuro-vid" target="_blank">
        <img src="/images/09.png" alt="Play Final Video">
      </a>
    </div>

    <div class="cta-btn-wrapper">
      <a class="cta-button" href="/neuro-vid" target="_blank">CLICK TO WATCH</a>
    </div>
"""

start_marker = '<main class="article-content">'
end_marker = '</main>'

start_idx = content.find(start_marker) + len(start_marker)
end_idx = content.find(end_marker, start_idx)

updated_content = content[:start_idx] + "\n" + new_article_content + "\n" + content[end_idx:]

with open('pressel/index.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

