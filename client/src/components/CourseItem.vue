<template>
    <q-item
            highlight
            separator
            link
            style='padding: 5px 10px;'
            @click.native="loadCourseDetails(); showModal = !showModal"
            @mouseover.native="hover()"
            @mouseleave.native="stopHover()"
    >
        <q-chip dense v-if="premajors.includes(course.code)" color="primary">
            Premajor
        </q-chip>

        <q-chip dense v-if="cores.includes(course.code)" color="secondary">
            Core
        </q-chip>

        <q-chip dense v-if="electives.includes(course.code)" color="tertiary">
            Elective/Advanced
        </q-chip>

        <q-chip dense v-if="prereqs.includes(course.code)" color="negative">
            Prerequisite
        </q-chip>

        <q-chip dense v-if="writings.includes(course.code)" color="warning">
            Writing
        </q-chip>
        <q-item-main style="margin-left: 3px">
            <small>{{stripString(courseString(course), lengthLimit)}}</small>
            <q-tooltip anchor="bottom middle" self="top middle">
                {{courseString(course)}}
                <br>
                {{details.prereq}}
            </q-tooltip>
        </q-item-main>
        <q-item-side right v-if="isRemoveable">
            <q-btn dense round flat icon="close" @click="onRemove(course)"/>
        </q-item-side>

        <q-modal v-model="showModal" :content-css="{maxWidth: '80vw', minHeight: '80vh'}">
            <q-modal-layout>
                <q-toolbar slot="header">
                    <q-toolbar-title>
                        {{courseString(course)}}
                    </q-toolbar-title>
                </q-toolbar>

                <div class="layout-padding">
                    <p class="q-title">Course Name</p>
                    <p>{{details.name}}</p>

                    <p class="q-title">Course Code</p>
                    <p>{{details.code}}</p>

                    <p class="q-title">Credits</p>
                    <p>{{details.credit_points}}</p>

                    <p class="q-title">Term(s)</p>
                    <p v-html="details.teaching_period"></p>

                    <p v-if="details.prereq" class="q-title">Prerequisite Course(s)</p>
                    <p v-html="details.prereq"></p>

                    <p class="q-title">Description</p>
                    <p v-html="details.description"></p>

                    <p class="q-title">Cluster(s)</p>
                    <p v-html="details.clusters"></p>
                </div>
            </q-modal-layout>
        </q-modal>
    </q-item>
</template>

<script>
    import axios from 'axios'

    export default {
        name: 'CourseItem',
        props: {
            course: {
                type: Object,
                required: true
            },
            lengthLimit: {
                type: Number,
                default: 35
            },
            isRemoveable: {
                type: Boolean,
                default: false
            },
            onRemove: {
                type: Function,
                default: function () {
                }
            },
            prereqs: {
                type: Array,
                default: () => []
            },
            premajors: {
                type: Array,
                default: () => []
            },
            cores: {
                type: Array,
                default: () => []
            },
            electives: {
                type: Array,
                default: () => []
            },
            writings: {
                type: Array,
                default: () => []
            }
        },
        data() {
            return {
                showModal: false,
                details: {},
                isLoaded: false
            }
        },
        methods: {
            hover: function () {
                this.loadCourseDetails();
                this.$emit('hoverCourse', this.course.code);
            },
            stopHover() {
                this.$emit('stopHoverCourse');
            },
            courseString: function (course) {
                return `${course.code} - ${course.name}`
            },
            stripString: function (str, limit) {
                if (str.length <= limit) {
                    return str
                }

                return str.substr(0, limit) + "..."
            },
            loadCourseDetails: function () {
                if (this.isLoaded) {
                    return
                }

                axios
                    .get(`${this.$config.API_BASE}/course-detail/${this.course.code}`)
                    .then(res => {
                        this.details = res.data
                        // eslint-disable-next-line
                        this.isLoaded = true
                    })
            }
        }
    }
</script>

<style lang="stylus">

    .q-chip
        margin-right 5px

</style>
