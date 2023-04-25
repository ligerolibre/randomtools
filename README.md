# randomtools
This Pyside project was created to create a fair and randomized song selection.

본 Pyside 프로젝트는 공정한 노래 선정을 위해서 마련되었습니다.

Change the items in the list variable in this code to use it.

list 변수의 항목을 변경하여 사용하세요.

It can be used not only for singing, but also in situations that require fairness, such as picking a lunch, picking a speaker, or picking a facilitator.

이 프로그램은 노래 선정을 위한 것만이 아닙니다. 점심 메뉴 결정이나 조별 과제의 발표자를 정하는 등 공정한 선정이 필요한 곳은 어디든 사용할 수 있습니다.

Pyside6 and Python3 must be installed to run.

프로그램 실행을 위해서는 Pyside6와 Python3가 설치되어 있어야 합니다.

# Key features 주요 기능
- Randomly select one
- Anti-tampering systems
- Clean design
- Built-in clock
- A 5-second timer (actually, it's 6 seconds) to create a sense of urgency.

- 무작위 선정
- 조작 방지 시스템
- 깔끔한 디자인
- 내장 시계
- 긴박감을 조성하기 위한 5초 타이머 (실제로는 6초랍니다!)

# How to use? 그래서 이걸 어떻게 쓰나요?
Change the items in the list variable (line 34)

list 변수의 항목을 변경하세요. (34번째 줄)
<pre><code># 노래 리스트
self.list = ["마침내 평화", "당신께 드려요", "결코 없어지지 않는 사랑", "하나로 연합된 우리", "이 기쁨 영원히"] # Change item
</code></pre>
Change the title of the window (line 16)

프로그램 창의 제목을 변경하세요. (16번째 줄)
<pre><code>self.setWindowTitle("🎤 노래 선정 시스템")
</code></pre>
For internationalization or design changes, please refer to the official Pyside6 documentation.

그 외의 국제화, 디자인 변경 등은 Pyside6의 공식 문서를 참고하시길 바랍니다.

This program is in Korean.

본 프로그램은 기본적으로 한국어로 작성되었습니다.

# How to Manipulate Probability 확률 조작하는 방법
The program is designed to prevent probability manipulation from occurring, but there may be situations where an item needs to be manipulated in its favor.

본 프로그램은 확률 조작이 발생하지 않도록 만들어졌으나 어느 항목이 유리하게 조작되어야 하는 상황이 있을 수 있습니다.

Guide to manipulating probabilities while evading anti-tampering systems.

조작 방지 시스템을 회피하면서 어떻게 확률을 조작할 수 있는지 안내합니다.

1. weights 변수를 만들고 가중치를 추가 합니다.

Create a 'weights' variable and add a weight item.
<pre><code>self.weights = [0.1, 0.4, 0.4, 0.05, 0.05]
</code></pre>

2. 159번째 줄에 위치한 <code>text = random.choice(self.list)</code> 코드를 다음과 같이 변경합니다.

Modify the code on line 159 to look like this:
<pre><code>text = random.choices(self.items, self.weights)[0]
</code></pre>

This code can be used for more than just probability manipulation.

이 코드는 단순히 확률 조작을 위해서만 사용되지 않습니다.

To further ensure fairness, you can set the weights to equalize to compensate for possible biases in the computing process.

더욱 공정성을 보장하기 위하여 가중치를 동일하게 설정하여 컴퓨팅 과정에서 발생 가능한 편향성을 보정할 수 있습니다.

# License 라이선스
<pre>Copyright (c) 2023 Seoyoungwoo.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.</pre>
