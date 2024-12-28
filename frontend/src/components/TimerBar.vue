<template>
    <section class="timerBar">
        <button @click="toggleButtons" class="timerButton" id="timerToggle"><img src="/images/timerToggle.svg"
                alt="Timer Options"></button>
        <button v-for="(time, index) in timerButtons" :key="index" class="timerButton"
            :class="{ active: activeButton === index, shown: true }" @click="toggleTimer(time.time, index)">
            <img :src="time.src" :alt="time.alt">
        </button>
    </section>
</template>

<script>
function toggleButtons() {
    const buttons = document.querySelectorAll('.timerButton');
    buttons.forEach((button, index) => {
        setTimeout(() => {
            button.classList.toggle('shown');
        }, index * 50);
    });
}

export default {
    name: 'TimerBar',
    props: {
        nextWord: Function
    },
    methods: {
        toggleButtons,
        disableTimer() {
            clearInterval(this.timerInterval);
            this.timerOn = false;
            this.activeButton = null;
        },
        intervalStart(time) {
            this.timerInterval = setInterval(() => {
                console.log(`Timer is on for ${time} seconds`);
                this.nextWord();
            }, time * 1000);
        },

        toggleTimer(time, index) {
            if (this.timerOn) {
                if (index != this.activeButton) {
                    if (time === "c") {
                        time = prompt("Enter a custom time in seconds");
                    }
                    clearInterval(this.timerInterval);
                    this.activeButton = index;
                    this.intervalStart(time)
                } else {
                    this.disableTimer()
                }
            } else {
                if (time === "c") {
                    time = prompt("Enter a custom time in seconds");
                    if (time === null) {
                        return;
                    }
                }
                this.timerOn = true;
                this.activeButton = index;
                this.intervalStart(time)
            }
        }
    },
    data() {
        return {
            timerButtons: [
                { src: '/images/timer1.svg', alt: "1 Second", time: "1" },
                { src: '/images/timer2.svg', alt: "2 Seconds", time: "2" },
                { src: '/images/timer3.svg', alt: "3 Seconds", time: "3" },
                { src: '/images/timer4.svg', alt: "4 Seconds", time: "4" },
                { src: '/images/timer5.svg', alt: "5 Seconds", time: "5" },
                { src: '/images/timerCustom.svg', alt: "Custom Timer", time: "c" }
            ],
            timerOn: false,
            activeButton: null
        };
    },
};
</script>

<style scoped>
.timerBar {
    display: flex;
    width: 100%;
    gap: .5rem;
}

.timerButton {
    display: flex;
    width: auto;
    height: 2.5rem;
    opacity: 0;
    user-select: none;
    pointer-events: none;
    transition: opacity 0.3s ease;
}

.timerButton:active {
    transform: scale(0.9);
}

.timerImg {
    width: auto;
    height: 100%;
}

.shown {
    opacity: 1;
    user-select: all;
    pointer-events: all;
}

#timerToggle {
    opacity: 1;
    user-select: all;
    pointer-events: all;
}

.timerButton.active img {
    filter: invert(50%) sepia(200%) saturate(500%) hue-rotate(90deg);
}

@media (min-width: 768px) {}
</style>