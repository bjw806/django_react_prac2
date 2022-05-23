import React, {useState, useEffect} from 'react';
import axiosInstance from '../../axios';
import {useParams} from 'react-router-dom';
import CssBaseline from '@material-ui/core/CssBaseline';
import {makeStyles} from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import CardMedia from "@material-ui/core/CardMedia";
import {Image} from "@material-ui/icons";
import Card from "@material-ui/core/Card";
import Link from "@material-ui/core/Link";

const useStyles = makeStyles((theme) => ({
    cardMedia: {
        paddingTop: '56.25%', // 16:9
    },
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
}));

export default function Post() {
    const {slug} = useParams();
    const classes = useStyles();

    const [data, setData] = useState({
        posts: [],
    });

    useEffect(() => {
        axiosInstance.get('post/' + slug).then((res) => {
            setData({
                posts: res.data,
            });
            console.log(res.data);
        });
    }, [setData]);

    return (
        <Container component="main" maxWidth="md">
            <CssBaseline/>
            <div className={classes.paper}></div>
            {' '}
            <div className={classes.heroContent}>
                <Container maxWidth="sm">
                    <Card className={classes.card}>
                        <CardMedia
                            className={classes.cardMedia}
                            image={data.posts.image}
                            title="Image title"
                        />
                        <Typography
                            component="h1"
                            variant="h2"
                            align="center"
                            color="textPrimary"
                            gutterBottom
                        >
                            {data.posts.title}{' '}
                        </Typography>{' '}
                        <Typography
                            variant="h5"
                            align="center"
                            color="textSecondary"
                            paragraph
                        >
                            {data.posts.content}{' '}
                        </Typography>{' '}
                    </Card>
                </Container>{' '}
            </div>
            {' '}
        </Container>
    );
}
